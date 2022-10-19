# This functions must be defined outside jupyter notebooks, otherwise they cannot be executed in separate processes.
import re

import praw
import unidecode

NON_ALPHANUMERIC = re.compile(r'[\W_]+')


# ============ DOWNLOADING OF POSTS ============

def download_and_prepare_posts(post_ids: list, praw_client_id, praw_client_secret, praw_client_ua):
    reddit = praw.Reddit(client_id=praw_client_id,
                         client_secret=praw_client_secret,
                         user_agent=praw_client_ua)
    fullnames = [f't3_{p_id}' for p_id, year in post_ids]
    retrieved_posts = set()

    for submission, (post_id, year) in zip(reddit.info(fullnames=fullnames), post_ids):
        title = submission.title
        post_text = submission.selftext

        if post_text != '[deleted]' and post_text != '[removed]':
            comments_fullnames = [f't3_{c_id}' for c_id in submission.comments.list()]
            all_comments = [comment_text for comment in reddit.info(fullnames=comments_fullnames) if
                            (comment_text := comment.selftext) != '[deleted]' and comment_text != '[removed]']
            comment_string = normalize_text(''.join(all_comments))

            retrieved_posts.add((post_id, year, normalize_text(title + post_text), comment_string))

    return retrieved_posts


# ============ COUNTING BOOK OCCURRENCES IN POSTS ============

def normalize_text(text: str) -> str:
    """
    Removes special characters, makes the string lowercase and returns the new string.
    """
    text = unidecode.unidecode(text)
    text = text.lower()
    text = re.sub(NON_ALPHANUMERIC, '', text)
    text = text.strip()
    return text


def count_occurrences_in_string(post_text, title_regex):
    occurrences = dict()
    post_text = normalize_text(post_text)

    # count occurrences of book titles in the text
    for match in title_regex.finditer(post_text):
        if (title := match.group(0)) in occurrences:
            occurrences[title] += 1
        else:
            occurrences[title] = 1

    return occurrences


def get_occurrences_for_post(post, title_regex):
    p_id, year, post_string, comment_string = post

    p_occ = count_occurrences_in_string(post_string, title_regex)
    c_occ = count_occurrences_in_string(comment_string, title_regex)

    return year, p_occ, c_occ
