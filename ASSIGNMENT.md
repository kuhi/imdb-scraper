# Data Scientist Python assignment

## Context

In our company, we work with various type of datasets, be it internal or external. In this case, we started a scraping project and gave our intern an IMDB website to scrape for top ranked movies. Unfortunately, he was only starting in Python and didn't do a very good job. At least he was able to identify important tag for scraping, which is `<tr>` Can you help him with it? We need our solution in 7 to 10 days. 

## What to do

1. Take the function at hand and improve it. We need to download relevant movies information and save it into `.csv` file. Visit IMDB to look at the source code of the page or look into picture attachment to guide you into what we are looking for. `movie name, actors, ranking, year of release` etc. The webpage you want to use is: http://www.imdb.com/chart/top
2. It would be nice if you could split the functionality into multiple files, for example `util.py` and `main.py` files. If you want to create a python object, go for it. 
3. If you want to use Jupyter Notebook/Lab, don't be afraid. We use them frequently.
4. Your code should be:
- working
- readable
- reliable
- useful
5. Be creative. There is not one correct solution. We just want to see that you are able to work with Python and create some useful result out of the useless code.
6. Don't give up. Ask google.
7. After you are done with your solution, please upload your solution to github. Write us an email, where you will describe what you did and send us an email with link to your repository, so we can check it.

## Hints

- What could happen in the script that it wouldn't work? could you implement some safety measures?
- Is it a good idea to implement version control in this code and put it to github?
- Can you think of some nice visualisations for movie ratings?
- What could be input parameters for this function? 
- Do you know about iterators? One was used in the original code, but they aren't very frequent. You can leave it or replace it as you like
- Have you heard about `argsparse`? It can help you in making the app usable from command line.
- Have you heard about `PEP8` in Python? Can you make the code more compatible?
- Libraries that could help you: `pandas`, `argparse`, `flake`
