[![App Deploys](https://github.com/UBC-MDS/nba_player_stat/actions/workflows/deploy-app.yaml/badge.svg)](https://github.com/UBC-MDS/nba_player_stat/actions/workflows/deploy-app.yaml)
[![App Deploys](https://github.com/UBC-MDS/nba_player_stat/actions/workflows/testing.yaml/badge.svg)](https://github.com/UBC-MDS/nba_player_stat/actions/workflows/testing.yaml)

# NBA Player Performances 

[Hosted on shinyapps.io](https://cchchechen.shinyapps.io/NBA_Player_Stats/)

***A comprehensive NBA player data visualization dashboard application.***

## Welcome!

Welcome to the repository of the NBA Performance App  :confetti_ball:  ！

Thank you for visiting our project,hope all of you can enjoy browsing the NBA player performance.

This document provides basic information of this NBA Player Performance.Please feel free to navigate each section by the list below: 

* [What are we doing?](#what-are-we-doing)
* [Description of App](#description-of-app)
* [Sketch](#sketch)
* [Contributors](#contributors)
* [How can you get involved?](#get-involved)

## What are we doing?

### The problem

How can we understand a NBA player's historical performance and skills during their career?


### The solution

The NBA performance app will:

* Improve visibility for the player's historical performance data.
* Help NBA fans better understand their favorite players and visualize how the players have performed historically over time and across players and teams.
* Let fans to determine a player's style such as what kind of player he is, how many games he plays, how much he scores per game, the number of assists, etc., and use this as a starting point to get to know a new player better. 

The most important thing is that we can honor and learn those former NBA superstars, such as Micheal Jordan and Kobe Bryant, by visualizing their performances. For instance, Kobe Bryant, we can learn about the wonders the legendary superstar created with the Lakers and the glory of the purple and gold dynasty with scored 33,643 points, 7,047 rebounds, and 6,306 assists during the entire career. Salute to the eternal Lakers #24.

## Description of App

The visualization app contains a landing page that shows NBA player performances. The visualization comprises the data of over 500 NBA players among 30 NBA teams. This app aims to help enthusiast NBA fans to understand better and assess NBA player performances.

The visualization is designed to display multiple statistics of NBA players. The app allows users to search for an interested NBA player by name with a search box item, for example, "Micheal Jordan", the app then shows the corresponding player's information. Furthermore. the users then are able to filter and scope the performances of the players with three types of filters,

- A slider of the year the player plays in NBA. 

- A check box of statistics to show.

- A check box of the team the player plays for. 

- A Tick box of the whole career statistics of the player.

We aim to offer three charts of player performances; Scoring performance(Point per game, Shooting accuracy), Game play(Number of games), and Skill indicators(Point per game, Total Rebound per game, Assist per game, Steal per game, and Block per game). These will show the player's performances according to the player search and its filter.

Therefore, users can study each NBA player's performance in detail and understand more about the player they are interested in.


## Sketch
<img src="img/dashboard_design_version4.png">

## Contributors
The contributors of this project are Peng Zhang, Fujie Sun, Chen Lin, and Nate Puangpanbut.

## Installation

To install `nba_player_stat` locally, you can:

1. Clone this repository with:

```
git clone https://github.com/UBC-MDS/nba_player_stat.git
```

2. Run the following command in your R console to install the required libraries locally:

```{r}
install.packages(c('tidyverse', 'dplyr', 'plyr', 'shiny', 'ggplot2', 'plotly', 'rvest', 'ggrepel', 'readr', 'RCurl', 'jpeg', 'thematic', 'httr', 'stringr', 'htmltools', 'devtools'))
```
```{r}
devtools::install_github("ricardo-bion/ggradar", 
                          dependencies = TRUE)
```

3. Finally, run the app locally by: 

- Open `Rstudio`, navigate to the project folder, open `app.R` and run it by clicking `Run` button on the top-right of RStudio.

- Open a command line, navigate to the project folder, run the following command to run the app locally:
    ```
    RScript app.R
    ```

## Get involved 

If you have any new ideas and suggestions for improvement about this app, please feel free to contact us. The main contact email is: althrunsun@gmail.com

Please note that it's very important to us that we maintain a positive and supportive environment for everyone who wants to participate. You can check the code of conduct for more details if you want to be with us.

# License
`nba_player_stat` is licensed under the terms of the MIT license.
Please refer to the License File [here](https://github.com/UBC-MDS/nba_player_stat/blob/main/LICENSE)
