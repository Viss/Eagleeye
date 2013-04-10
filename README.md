The EagleEye project
By Viss!
:::

Update: April 10, 2013:
I've included my generic 'shodan turk' script. 
It's a fairly simple tool that will allow you to point it
at shodan, search for something, then 'do something' with
the results.
Please enjoy!

*** NOTICE***
Paul R has done an epic job of taking my horrifically bad code and making it awesome
His repository can be found here:

https://github.com/PaulMcMillan/eagleeye_ce

I'd strongly suggest using HIS code rather than mine at this point - its MUCH more robust, faster, etc.

****</notice***

So I've done a bunch of research in the last couple years
about finding silly things on the internet and part of those
logistics is to find a way to efficiently look at something
like ten to a hundred thousand websites in a short period
of time. 

Well - lets say that browsers don't do so well with that many
tabs. 

Meet WkHTMLtoImage - it's a tool that will take screenshots
of websites! That's pretty damn cool if you ask me. 

So this is a wrapper for it, basically. 

At the moment, its got the shodan API built in so that one 
can run it against specific results of a shodan search.

In the future I can see it being useful as an internal tool
for people or shops that have tens of thousands of hosts
that devs sort of do 'whatever they want' on, and there needs
to be some accountability by the security team (like how many
naked jboss or tomcat installs are there with default creds?)

Any help towards those goals will be graciously appreciated
and thanks will be paid in favors, beer, and things that 
are too spicy for regular people to think about!
 
