photocrypt
==========

Photocrypt / Tomestone #HackMIT2013

In this hack we wanted to add client side encryption to dropbox and at the same time make it possible to seamlessly share any of those encrypted photos with friends and family without revealing the key or revealing other images. To do so, we introduced a new application for a cryptographic technique referred to as convergent encryption. Using this method, each time user needs to share a photo, he can easily generate a new key specific to that single photo and send that key to users along with the link to the photo. We also used javascript crypto APIs to make it possible to decrypt the photo on any device and on the client side, so we won't ever need to share the key with the server.
This project was a part of HackMIT 2013. Contributors: Patricia Hanus, Henry Fanson, Andrew Lavery, and Mahrud Sayrafi.
http://hackmit.challengepost.com/submissions/17934-photocrypt

http://tomestone-hfans.rhcloud.com/s/73dk1br7h7jknhe/first.jpg.enc#hkey:yellowsubmarines
http://tomestone-hfans.rhcloud.com/s/73dk1br7h7jknhe/first.jpg.enc#skey:bbf58c0f5a6bbd39df420030ef15314a929f355745340a3e35728530c7ba17ac

http://tomestone-hfans.rhcloud.com/s/z87cxueqrh1adht/secret.txt.enc#hkey:xfiles
http://tomestone-hfans.rhcloud.com/s/z87cxueqrh1adht/secret.txt.enc#skey:659a28658a4641ab6f7cad5a78ecf1147262eff960537663a5ab15bbcc385572
