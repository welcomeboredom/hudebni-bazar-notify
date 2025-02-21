# hudebnibazar.cz scraper

Script for scraping hudebnibazar.cz on regular basis in cronjob manner. Matches newly appeared gear based on the keywords, checks if given advertisement has already been processed and pushes notification through Spontit.

## How to use

 - Setup `config.yml` file with PushNotifier credentials for app:

```
pushnotifier:
username: ""
password: ""
package: ""
api_token: ""

hudebnibazar:
base_url: "https://hudebnibazar.cz"
scrape_url: "https://hudebnibazar.cz/kytary/110000/"
keywords:
    - "chase"
    - "neunaber"
    - "distortion"
    - "chorus"
```

 - Venv create `python3 -m venv .venv`
 - Venv activate `.venv/bin/activate`
 - Install requirements `pip3 install -r requirements.txt`
 - Run manually `/usr/local/bin/python3 hudebnibazar.py`
 - Configure cronjob with `crontab -e` -> `*/5 * * * * cd /Users/<USERNAME>/scripts/hudebni-bazar-notify && curl https://hudebnibazar.cz/kytary/110000/ > hudebni_bazar_result.html && .venv/bin/python3 hudebni-bazar-notify.py >/tmp/cron.log 2>/tmp/cron.log`

## TODO

 [] configure as AWS lambda cron function
 [] save links_seen to i.e. dynamodb or firestore
 [] statistics - parse product names etc. LLM maybe
 [] get rid of base_url variable (parse it from scrape URL)