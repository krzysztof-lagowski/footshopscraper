
![Logo](https://i.imgur.com/IDLpgPi.png)


# Description

This tool can scrape the stock and sizes of every raffle which is listed on: https://releases.footshop.com/ The stock is posted as a webhook in your Discord channel.
If you know the stock you can enter the sizes with most stock to create a bigger chance of winning.



## Features

First, create a [discord bot](https://www.youtube.com/watch?v=j_sD9udZnCk)

Second, create a [discord webhook](What Is a Webhook & How to Create Webhooks on Discord)


Then you need to install packages so you can run the Python file
- ```pip install requests```
- ```pip install bs4```
- ```pip install discord_webhook```
- ```pip install discord```

After all these steps you can insert your **bot token** and **webhook link** into the code. (line 6&7)

# Usage

- Get your desired link e.g. https://releases.footshop.com/nike-dunk-low-retro-qs-PGaHRYMB3xHSyCfZQxJJ
- Copy the ID (last part of the link), in this case ```PGaHRYMB3xHSyCfZQxJJ```
- write **!scrape ID** e.g. ```!scrape PGaHRYMB3xHSyCfZQxJJ```

![Logo](https://i.imgur.com/jMhyA5x.png)
