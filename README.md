# Book Ranking for r/books

I analyzed how often book titles occur in the subreddit [r/books](https://reddit.com/r/books).
The ranking is based on all posts posted before 2022-09-31 (546,219 posts of which 289,581 posts were already removed or deleted).


## Results
![](Graphics/Top-10.png)
![](Graphics/Top11-20.png)

<details>
<summary>Click to view the top 100 most often occurred books</summary>

|     | Title                                |   Occurrences |
|----:|:-------------------------------------|--------------:|
|   1 | Harry Potter                         |          3151 |
|   2 | 1984                                 |          2232 |
|   3 | The dark tower                       |          1395 |
|   4 | The Lord of the Rings                |          1225 |
|   5 | The Hunger Games                     |          1176 |
|   6 | Bible                                |          1067 |
|   7 | Infinite jest                        |          1045 |
|   8 | The Hobbit                           |           999 |
|   9 | Twilight                             |           925 |
|  10 | Catcher in the Rye                   |           882 |
|  11 | Ulysses                              |           872 |
|  12 | Brave New World                      |           866 |
|  13 | Carrie                               |           817 |
|  14 | Lolita                               |           817 |
|  15 | Ender's Game                         |           807 |
|  16 | Frankenstein                         |           783 |
|  17 | The Great Gatsby                     |           778 |
|  18 | Moby Dick                            |           776 |
|  19 | Crime and Punishment                 |           741 |
|  20 | House of Leaves                      |           716 |
|  21 | The Count of Monte Cristo            |           709 |
|  22 | To Kill a Mockingbird                |           707 |
|  23 | The Shining                          |           702 |
|  24 | War and Peace                        |           684 |
|  25 | Catch-22                             |           682 |
|  26 | East of Eden                         |           681 |
|  27 | The Martian                          |           652 |
|  28 | A Song of Ice and Fire               |           626 |
|  29 | Fahrenheit 451                       |           612 |
|  30 | Brothers Karamazov                   |           601 |
|  31 | Dracula                              |           591 |
|  32 | The hitchhiker's guide to the galaxy |           546 |
|  33 | Don Quixote                          |           539 |
|  34 | Animal Farm                          |           538 |
|  35 | Sherlock Holmes                      |           529 |
|  36 | Pride and Prejudice                  |           523 |
|  37 | American Gods                        |           521 |
|  38 | Slaughterhouse-Five                  |           498 |
|  39 | The Odyssey                          |           494 |
|  40 | American Psycho                      |           490 |
|  41 | Anna Karenina                        |           477 |
|  42 | Ready Player One                     |           475 |
|  43 | The Name of the Wind                 |           458 |
|  44 | Jane Eyre                            |           455 |
|  45 | Atlas Shrugged                       |           454 |
|  46 | Misery                               |           445 |
|  47 | A Little Life                        |           438 |
|  48 | Hyperion                             |           433 |
|  49 | The Alchemist                        |           427 |
|  50 | The Handmaid's Tale                  |           415 |
|  51 | The Sandman                          |           406 |
|  52 | The Witcher                          |           403 |
|  53 | 11/22/63                             |           403 |
|  54 | Fight club                           |           388 |
|  55 | 50 Shades of Grey                    |           387 |
|  56 | Lord of the Flies                    |           377 |
|  57 | The Grapes of Wrath                  |           356 |
|  58 | Neuromancer                          |           350 |
|  59 | Kafka on the Shore                   |           347 |
|  60 | Wuthering Heights                    |           337 |
|  61 | Gone Girl                            |           336 |
|  62 | Flowers for Algernon                 |           336 |
|  63 | The secret history                   |           336 |
|  64 | A Clockwork Orange                   |           324 |
|  65 | Of Mice and Men                      |           320 |
|  66 | Norwegian wood                       |           319 |
|  67 | Hamlet                               |           317 |
|  68 | Cat's Cradle                         |           313 |
|  69 | Jurassic Park                        |           308 |
|  70 | Divergent                            |           298 |
|  71 | One Hundred Years of Solitude        |           296 |
|  72 | The inferno                          |           290 |
|  73 | Eragon                               |           288 |
|  74 | The metamorphosis                    |           287 |
|  75 | The Stormlight Archive               |           286 |
|  76 | Circe                                |           284 |
|  77 | His Dark Materials                   |           280 |
|  78 | Cloud Atlas                          |           279 |
|  79 | The Way of Kings                     |           266 |
|  80 | The Book Thief                       |           262 |
|  81 | World War Z                          |           257 |
|  82 | The old man and the sea              |           253 |
|  83 | Les Misérables                       |           252 |
|  84 | Project Hail Mary                    |           247 |
|  85 | Kite Runner                          |           246 |
|  86 | The Picture of Dorian Gray           |           245 |
|  87 | Heart of Darkness                    |           243 |
|  88 | Red Rising                           |           242 |
|  89 | The Goldfinch                        |           237 |
|  90 | Salem's Lot                          |           235 |
|  91 | Never let me go                      |           234 |
|  92 | The Silmarillion                     |           232 |
|  93 | Faust                                |           232 |
|  94 | The Song of Achilles                 |           229 |
|  95 | The Fountainhead                     |           226 |
|  96 | Snow Crash                           |           222 |
|  97 | And Then There Were None             |           221 |
|  98 | Wind-Up Bird Chronicle               |           218 |
|  99 | Do Androids Dream of Electric Sheep? |           217 |
| 100 | Good Omens                           |           215 |

</details>


## How It Works
### Stage 1 - Prepare Books

[Stage_1-BooksPreparation.ipynb](Stage_1-BooksPreparation.ipynb)

Analyze the book dump from OpenLibrary and remove all duplicates and ambivalent book titles.


### Stage 2 - Find the IDs of all Posts that were posted in the Subreddit

[Stage_2-ScrapeAllPostIDs.ipynb](Stage_2-ScrapeAllPostIDs.ipynb)

Download the ID of every post that was posted in the subreddit via the PRAW API.


### Stage 3 - Download all Posts

[Stage_3-DownloadAndPreparePosts.ipynb](Stage_3-DownloadAndPreparePosts.ipynb)

Use the previously collected IDs to download the post texts. All posts marked as deleted or removed are discarded.


### Stage 4 - Count how often the Book Titles occur in the Posts

[Stage_4-CountBookTitlesInPosts.ipynb](Stage_4-CountBookTitlesInPosts.ipynb)

Generate a regular expression from the book titles and count the largest non-overlapping occurrences for each book title.


### Stage 5 - Clean the resulting Book Counts

[Stage_5-CleanUpBookRanking.ipynb](Stage_5-CleanUpBookRanking.ipynb)

There are many book titles that cannot be uniquely identified as book titles (e.g. 'It' by Stephen King) that have to be removed.

The final book ranking is based on the cleaned ranking.


### Stage 6 - Generate Graphics

[Stage_6-CreateGraphics.ipynb](Stage_6-CreateGraphics.ipynb)

Use the collected data to generate a few plots and automatically update the ranking in this README.md.
