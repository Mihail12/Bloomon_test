Hey, this is my solution of the test that have been declared in ./requirements.pdf

Thanks, it was really interesting and kind of challenging, it was pleasure to solve it

please give me feedback if I miss something or did something in strange way I will explain. my contact: spasenkomihail@gmail.com

Start
---
As you asked i did Dockerfile for start the test in docker. To start it, you should:

`docker build -t bloomon .`

than

`docker run bloomon`

-
if you prefer docker-compose

than please type:

`docker-compose up`

Results
---
You will see results in bouquet_shop/orders.txt
Note: for some reasons `docker run bloomon` do not respect VOLUME (or i do not find how to do it right)
and in this start do not save orders.txt on machine and you couldn't see it after run

or right in terminal


Note
---
There ara 2 dict im my solution small_flowers and large_flowers and also small_bouquet and large_bouquet
and maybe it will be better to do it in one dictionary and use something like 'aL' or 'dS' as a key
but i found it a bit of complex and less readable and also it not really boost the speed of compute