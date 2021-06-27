LobbySpy

Simple little tool I made to show who's in a Heroes of Hammerwatch Lobby without having to join. 
you need galaxy debug logs enabled for this to work, to do that, create a file called `GalaxyPeer.ini` inside your Heroes of Hammerwatch Game folder and put the following in it:

```
# LOCAL GALAXY PEER CONFIG

[DEFAULT]
Logging.appenders = File

Logging.Appender.File.level = DEBUG
Logging.Appender.File.type = file
Logging.Appender.File.filename = GalaxyPeer.log
Logging.Appender.File.truncate = true
```

The list should update on lobby refreshes, if using on windows, to get it to clear the screen properly with each refresh i think you'll need to change line 22 to 
`			os.system("cls")`

![image](https://user-images.githubusercontent.com/8881764/123543015-90156000-d744-11eb-9766-1337eef846d7.png)
