SMS & Email Bomber 
====================

A lightweight SMS &amp; Email Bomber, made in Python by the great cxdy
and expanded upon by the lesser UncleBenis


Requirements
====================

Python 2.7.6
or 
Soon: Python 3.x

(more than one preferred, since most SMS apps are threaded)

Add your email accounts to accounts.txt in the following format:

youraddress@ser.ver:yourpassword

OR

ilovethedisabled@gmail.com:heilhotwheels

Personal Appeal
===================

I must ask that you do NOT use cock.li. There are plenty of other services that you can use and using cock.li causes a lot
of grief to vc, who provides a very useful service to all of us. Our community appreciates his work too much to abuse the service provided, so if you can
donate to that service, and spread the love. Use gmail or something for your abuse needs, nobody likes google anymore, anyway. thanks, finn.

Usage
====================
1. With a file option passed to it, like such

$ python smsbomber.py targetfile

2. or, just by being called with

$ python smsbomber.py

For Method 1: See Target Files


For Method 1:

	1. Run it.
	2. Follow the on-screen prompts.
	3. Use numbers to navigate.


Target Files
===================

To create a target file, see the syntax at the top of smsbomber.py



Adding carriers
====================

Carrier list can be found here; http://www.emailtextmessages.com/

If you desire to add a carrier, find the last carrier in the list at the top and add one to it's number.

For example, the last carrier on the list should be 9. In this case, you will add to that list a 

12. Carrier Name
 

and then you will go down to the carriers[] array, and add:

, "txt.carrier.tld"


If you would like any new carriers added to the main client, create an issue for it and I will add them. In the mean time, you can use the above format for adding them to your local branch.
