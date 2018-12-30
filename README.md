# <img src='https://rawgithub.com/FortAwesome/Font-Awesome/master/advanced-options/raw-svg/solid/flag-checkered.svg' card_color='#40DBB0' width='50' height='50' style='vertical-align:bottom'/> Finished Booting Skill
Skill to determine when Mycroft AI has finished booting up.

## About 
With this skill Mycroft will say "finished booting" or play a startup sound when the boot up period has finished and is ready to receive commands. 

## Examples 

## Credits 
zelmon64 (@zelmon64), Wally Fort (@fortwally), JarbasAI (@JarbasAI)

## Category
**Configuration**

You may optionally add a configuration stanza to mycroft.conf to play an mp3 file instead of speaking:
```
  "FinishedBootingSkill": {
    "startup_mp3": "/home/pi/chimes-1948.mp3"
  }
```

## Tags
