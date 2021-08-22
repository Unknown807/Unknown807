import os
import json
from datetime import datetime
from github import Github

g = Github(os.environ["access_token"])
user = g.get_user("Unknown807")

with open("colours.json", "r") as f:
    lang_colours = json.load(f)

all_langs = {}

for repo in user.get_repos():
    langs = repo.get_languages()
    
    for k in langs.keys():
        all_langs[k] = all_langs.get(k, 0) + langs[k]

sorted_langs = sorted(all_langs, key=lambda x: all_langs[x])[::-1]

top_5_langs = sorted_langs[:5]
top_5_total = sum([v for k, v in all_langs.items() if k in top_5_langs])

other_langs = sorted_langs[5:]
other_total = sum([v for k, v in all_langs.items() if k in other_langs])

for k, v in all_langs.items():
    chosen_total = other_total
    if k in top_5_langs:
        chosen_total = top_5_total

    all_langs[k] = round(v/chosen_total*100, 1)

sorted_langs = sorted(all_langs, key=lambda x: all_langs[x])[::-1]

other_langs_anim = """"""
other_langs_div = """"""
other_langs_legend = """"""

top_5_langs_anim = """"""
top_5_langs_div = """"""
top_5_langs_legend = """"""

for lang in other_langs:
    other_langs_anim += """
    #{0}perc {{
        background: {1};
    }}

    #{0}text {{
        color: {1};
        font-size: 24px;
    }}
    """.format(lang, lang_colours[lang]["color"])
    
    other_langs_div += """
    <div id="{}perc">{}%</div>
    """.format(lang, all_langs[lang])

    other_langs_legend += """
    <div id="{0}text">{0}</div>  
    """.format(lang)

for lang in top_5_langs:
    top_5_langs_anim += """
    #{0}perc {{
        background: {1};
    }}

    #{0}text {{
        color: {1};
        font-size: 24px;
    }}
    """.format(lang, lang_colours[lang]["color"])
    
    top_5_langs_div += """
    <div id="{}perc">{}%</div>
    """.format(lang, all_langs[lang])

    top_5_langs_legend += """
    <div id="{0}text">{0}</div>  
    """.format(lang)

svg = """<svg style="background-color: white;" fill="none" viewBox="0 0 500 400" width="500" height="400" xmlns="http://www.w3.org/2000/svg">
    <foreignObject width="100%" height="100%">
        <div xmlns="http://www.w3.org/1999/xhtml">
        
            <style>
                h3 {{
                    font-family: 'San Francisco', 'SNFS Display', BlinkMacSystemFont, "Segoe UI", Roboto, 
      Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
                }}

                #top-5-langs div,
                #other-langs div {{
                    color: white;
                    font-family: sans-serif;
		    font-weight: bold;
		    font-size: 12px;
		    line-height: 20px;
		    display: flex;
		    align-items: center;
		    justify-content: center;
		}}

		#top-5-langs,
		#other-langs {{
		    border-radius: 5px;
		    overflow: hidden;
		    display: grid;
		}}

		#top-5-langs {{
                    grid-template-columns: {0};
		}}

		#other-langs {{
                    grid-template-columns: {1};
		}}

                .legend {{
                    display: grid;
                    grid-gap: 10px;
                    grid-template-columns: repeat(3, 1fr);
                }}
            
                {2}
                {3}
            </style>

            <h3>My Top 5 Used Languages</h3>
            
            <div id="top-5-langs">
                {4}
            </div>

            <br />
            
            <div class="legend">
                {5}
            </div>

            <h3>My Other Used Languages</h3>
            
            <div id="other-langs">
                {6}
            </div>

            <br />
                
            <div class="legend">
                {7}
            </div>
        
        </div>
    </foreignObject>
</svg>""".format(
    "fr ".join([str(all_langs[l]) for l in top_5_langs])+"fr",
    "fr ".join([str(all_langs[l]) for l in other_langs])+"fr",
    other_langs_anim,
    top_5_langs_anim,
    top_5_langs_div,
    top_5_langs_legend,
    other_langs_div,
    other_langs_legend,
)

with open("languages.svg", "w") as f:
    f.write(svg)

new_readme = """## Hi There 👋

Last Updated: {}

I've always been interested in creating new and optimal solutions to problems I encounter. It has led me to become interested in programming and new practical technologies and passionate about Computer Science overall.

I create many personal projects and always do a lot of planning, research and design. Here are the languages I have used the most:

<div align="center">
    <img src="languages.svg" width="500" height="350" alt="language-stats-here">
</div>

<br />

One of my favourite games to play is Hearthstone, so I made a fun pack opening activity using Github Actions and Python. Click to open any one of the packs from my favourite parts/expansions of the game to date:

<div align="center">
  
  <div style="display:flex;">
    <div style="flex:33.33%;padding:5px;">
      <a href="https://github.com/Unknown807/Unknown807/issues/new?title=open%20pack%7Cclassic&amp;body=Just+push+%27Submit+new+issue%27+and+open+a+new+pack+and+please+wait">
          <img src="/packs/classic_pack.webp" width=160 height=200/>
      </a>
      <a href="https://github.com/Unknown807/Unknown807/issues/new?title=open%20pack%7Cgrandt&amp;body=Just+push+%27Submit+new+issue%27+and+open+a+new+pack+and+please+wait">
          <img src="/packs/gt_pack.webp" width=160 height=200/>
      </a>
      <a href="https://github.com/Unknown807/Unknown807/issues/new?title=open%20pack%7Cwotog&amp;body=Just+push+%27Submit+new+issue%27+and+open+a+new+pack+and+please+wait">
          <img src="/packs/og_pack.webp" width=160 height=200/>
      </a>
    </div>
  </div>

</div>
""".format(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))

with open("README.md", "w") as f:
    f.write(new_readme)
