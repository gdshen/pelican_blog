Title:tmux使用小结
Date:February 13, 2015 2:24 PM
Category:linux
Tags:linux, vps

# 使用tmux代替screen
以前一直使用screen来做freeshell上的远程会话管理,但是screen不支持zsh上的一些主题,这个看着很不舒服.后来找到screen同类型的代替品tmux,试用一下感觉很不错.

### tmux的简单使用方法
1. 新建会话 `tmux new-session -s session-name`
2. 重新连接会话 `tmux attach-session -t session-name`
3. 显示所有会话 `tmux ls`

