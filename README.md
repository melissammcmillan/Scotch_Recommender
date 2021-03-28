## Scotch Recommender: My Passion Project

This project was released on 3/26/2021, and is meant to represent a Minimum Viable Product, so there isn't much fluff/sparkle yet. Here is the link to the Streamlit App: https://share.streamlit.io/melissammcmillan/scotch_recommender/main/Recommender_App.py

### Table of Contents
Below is a table of contents, which contains the folder name, folder order, file name, file order, and file description. The file order column represents which order the files should be opened and read. Folder 0, File Order 1 should be started with.


**Folder Name**|**Folder Order**|**File Name**|**File Order**|**File Description**
:-----:|:-----:|:-----:|:-----:|:-----:
Main|0|README.md|1|The README file contains the executive summary and overview of the project as a whole.
Main|0|requirements.txt|2|These are the libraries with versions that go into the Streamlit App.
Main|0|Recommender_App.py|3|This is the code for my Streamlit App.
code|1|01_Clean_and_EDA.ipynb|1|In this notebook I clean the data and do some simple EDA.
code|1|02_K_Means_Clustering_Analysis.ipynb|2|In this notebook I experiment with clustering to find the "right" number of clusters for this dataset.
code|1|03_Prep_for_App.ipynb|3|This notebook contains some experimentation as prep for the Streamlit App.
data|2|whisky.csv|1|This is the raw dataset downloaded from Kaggle.
data|2|labelled_distilleries.csv|2|This is the raw dataset with labels added after the cluster analysis. This is the dataset used in the Recommender_App.py file.
assets|3|drink-3108435_1920.jpg|0|This is the image used for the background in the Streamlit App.


#### The Problem and The Solution
I became a big fan of scotch whisky a few years ago, and trying new scotches with friends is one of my favorite activities (pre-pandemic, of course!). In trying lots of different scotches, I've learned that I am VERY picky about which ones I like: they have to be on the extreme end of the smoky/peaty/medicinal scale. If it's not smoky, I don't like it. While this was a fascinating discovery for my husband and me, it created sort of a problem because I'm really picky now, and of course, I like the really expensive scotches (why go for the 12 year when the 18 year is so much better?). So, I'm not really a fan of just buying random random scotches from our favorite liquor store: I want to know that I will probably like the scotch I purchase instead of taking a gamble. That's where this Scotch Recommender comes in! I have been wanting to make a recommender, specifically for scotch, for a few months now, but hadn't really had the time. Truly, I made this recommender for my own personal use, but I'm also excited to share it with friends, family, colleagues, etc so it can be utilized and improved.

I gave myself one week to put this project together from scratch to see how far I could get. My goal was to find a scotch dataset, use an algorithm to group the scotches together, and make a Streamlit App to provide the recommendations. While I consider this project a success, there's quite a bit of work still to be done. I'd consider this a Minimum Viable Product, and I'm excited to continue working on it.


#### Data Acquisition and Preprocessing
As this was planned to be a one-week project, I needed to find a dataset that was mostly put together and ready-to-use. I didn't have a ton of time to scrape data from various sources, and the cleaner it came the better. That's why I decided to use this Kaggle dataset: https://www.kaggle.com/koki25ando/scotch-whisky-dataset. It's definitely a starter dataset in that it has scotches defined by distillery, not necessary individual batches/bottles, but for a one-week project it was good enough. And it was pretty clean, so I felt like I could quickly get to the grouping/recommender modelling portion of the project.

As a high-level overview, each scotch/distillery is broken down by flavor profile, with each type of flavor given a rating from 0 to 4. Zero indicates low levels of the flavor, four means highest level of flavor. The flavor profiles given in the dataset are: Body, Sweetness, Smoky, Medicinal, Tobacco, Honey, Spicy, Winey, Nutty, Malty, Fruity, and Floral. The dataset also came with Latitude and Longitude of the distillery, but I chose not to use that information for now in order to narrow the scope of the project so I could fit it into one week. I would like to go back in and use this information later, as it could prove interesting to explore.


#### EDA and Findings
Once I began to sort the scotches by their flavor profiles, for example looking at the scotches with Smoky > 2, I could see that there were patterns where the distilleries could be grouped together. There were many scotches where the Sweetness and Floral/Fruity flavors were scored highly and those scotches did not overlap with the most Smoky/Medicinal scotches. This kind of exploration can be seen in the 01_Clean_and_EDA notebook. After this experimentation, it occurred to me that I could probably use a simple K Means Clustering algorithm to try sorting/clustering these scotches together using the flavor profile data, so that's what I did.

#### Final Production Model
Using the elbow method, I experimented with K Means Clustering and found that the optimal number of clusters was ~3-4. I experimented with both 3 clusters and 4 clusters, and it seemed like 3 clusters gave the best/most logical groupings of the scotches. With 3 clusters, it was very clear which flavor profiles were driving the groupings. Group 0 contains the Honey, Spicy, Winey flavors that have some Fruity, Floral, Nutty flavor profiles. These scotches have lots of body. Group 1 contains the high Medicinal/Smoky scotches with high Body/Flavor, and Group 2 contains the Sweet/Fruity, Floral, and Nutty flavors that are more subtle (less Body). These are the categories I saved and used directly in the Recommender App.


#### The Conclusion
My quest to cluster scotches and turn the results into a recommender were successful. One can very easily access the App I made (link above), and ask for a recommendation either based on a distillery they already enjoy or pick the category they are in the mood for. While there is definitely room for improvement in this project, this is great start for my first recommender project. Any and all feedback is welcome!


#### Improvements and Future Work
Though my initial product was successful, there are many aspects of this project I'd like to improve. First, I'd like to get a bigger dataset that includes specific bottles/casks/ages instead of grouping by distillery. I'd also like to experiment with different clustering algorithms (like DB Scan) to see if that does any better with grouping the existing data. Additionally, there are lots of improvements to make on the App itself. It's very plain-looking right now, so I'd like to make it prettier. There are many functionality improvements to make as well, including a map that shows where the distilleries in each group are located, and I'd like to make radar/spider plots for each scotch the user selects so the flavor profiles can be compared. LOTS and LOTS of work left to do!


#### Citations & Sources
1. https://www.kaggle.com/koki25ando/scotch-whisky-dataset
2. https://whiskyanalysis.com/index.php/methodology-introduction/methodology-flavour-comparison/
