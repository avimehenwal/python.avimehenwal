# -e ----> Enables backslash escape sequences
# In bash, <ESC> character is obtained by followinf syntaxes
# \e
# \033
# \x1B
# https://misc.flogisoft.com/bash/tip_colors_and_formatting
# http://wiki.bash-hackers.org/scripting/terminalcodes
# ftp://ftp.iitb.ac.in/LDP/en/Bash-Prompt-HOWTO/Bash-Prompt-HOWTO-single.html
# https://wiki.archlinux.org/index.php/Bash/Prompt_customization
# 

echo -e "\033[31mHello\e[0m World"
for i in {16..21} {21..16} ; do echo -en "\e[48;5;${i}m \e[0m" ; done ; echo
for i in {16..21} {21..16} ; do echo -en "\e[38;5;${i}m#\e[0m" ; done ; echo

#Background
for clbg in {40..47} {100..107} 49 ; do
	#Foreground
	for clfg in {30..37} {90..97} 39 ; do
		#Formatting
		for attr in 0 1 2 4 5 7 ; do
			#Print the result
			echo -en "\e[${attr};${clbg};${clfg}m ^[${attr};${clbg};${clfg}m \e[0m"
		done
		echo #Newline
	done
done

exit 0

for fgbg in 38 48 ; do # Foreground / Background
    for color in {0..255} ; do # Colors
        # Display the color
        printf "\e[${fgbg};5;%sm  %3s  \e[0m" $color $color
        # Display 6 colors per lines
        if [ $((($color + 1) % 6)) == 4 ] ; then
            echo # New line
        fi
    done
    echo # New line
done

exit 0
