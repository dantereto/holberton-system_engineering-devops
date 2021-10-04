<center> <h1> postmortem </h1> </center>

<center> <h1> Issue Summary </h1> </center>

We found an access problem when trying to enter a server
from 2:35 PM to 3:03 PM PT using curl which caused that
it could not be accessed and preventing any user from entering,
the root cause of this outage it was a problem to enable the nginx server.

<center> <h1> Timeline </h1> </center>

-2: 35 PM: the problem start
-2:38 PM: Pagers alerted teams
-2:45 PM: Failed configuration change rollbak
-2:50 PM: Successful configuration rollback
-2:55 PM: Server restarts begin
-3:03 PM: 100% of traffic bask online

<center> <h1> Root cause and resolution </h1> </center>

the problem is that in the nginx folder in
/etc/nginx/ sites-enabled/default,
the port 8080 was not enabled correctly,
so the server we needed could not be
accessed and therefore could not be accessed.
This problem was fixed with the 'sed' command
that allows us to fix the path to the port we
need and thanks to that we get access. finally
you have to restart the nginx service to save the changes

<center> <h1> Corrective and preventative measures </h1> </center>

to prevent problems like these, make sure you
know which port the server you want to access
belongs to in order to allow access or have the nginx well prepared.
In conclusion we must take into account:
patch Nginx server, good monitoring on the path
and the assurance of what kind of server you want to access.