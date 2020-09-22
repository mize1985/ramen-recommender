# Chubu Region Noodle Shop Recommender
---

This folder contains files used for scraping comments from Tabelog, tokenizing, count vectorizing, topic modeling, and recommending noodle shops based on those comments.

## tabelog_scraper

Scrapes Tabelog for combinations of regions and genres of food.

## noodle_shop_nlp

Does tokenizing, vectorization, and topic modeling. It requires MeCab installation to run.

## ./webapp

Contains web application files that use the output of the model to recommend noodle shops.

## ./media

Contains image files related to the presentation of this project.