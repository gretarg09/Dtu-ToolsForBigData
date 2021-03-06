import timeit
import queries_IBE_cython as cy


cy.main("cat[0, 10]are[2, 6]to")
cy.main("or[6, 7]or[2, 6]or")
cy.main("when[6, 7]republic[2, 6]along")



# ---------- For the cat article ----------

#cy.main('cat[0, 10]are[0, 10]to')
# Got 1 results and 10 matches
# We got 1 result and 10 matches  ----

#cy.main('cat[0, 100]anatomy')
# Got 1 results and 11 matches
# We got 1 results and 11 matches ----

#cy.main('china[30, 150]washington')
# Got 1 results and 1 matches
# We got 1 result and 1 matches ----

#cy.main('english[0, 200]cat')
# Got 1 results and 37 matches
# We got 1 results and 37 matches  ----

#cy.main('kitten[15, 85]cat[0, 100]sire[0, 200]oxford')
# Got 1 results and 2 matches
# We got 1 results and 2 matches ----


# ----------- Letter query -----------
#"A" articles - picked as all articles starting with letter "A" or "a"

#cy.main('arnold[0,10]schwarzenegger[0,10]is')
# Got 5 results and 15 matches
# We got 5 results and 14 matches

#cy.main('apache[0, 100]software')
# Got 186 results and 1517 matches
# We got got 186 matches and 1517 matches ----

#cy.main('aarhus[30, 150]denmark')
# Got 131 results and 555 matches 
# We got 131 results and 554 matches

#cy.main('english[0, 100]alphabet')
# Got 92 results and 181 matches ----
# We got 92 results and 181 matches

#cy.main('first[0, 85]letter[0, 100]alphabet[0, 200]consonant')
# Got 3 results and 3 matches
# We got 3 results and 3 matches ----

# ----------- All articles -----------

#All articles (around 5 463 000)
#cy.main('elephants[0,20]are[0,20]to')
#Got 126 results and 181 matches
# we got 126 and 181 matches ----

#cy.main('technical[0, 20]university[0, 20]denmark')
# Got 408 results and 611 matches
# we got 408 results and 611 matches   ----

#cy.main('testing[0, 20]with[0, 20]a[0, 30]lot[0, 4]of[0, 5]words') 
#Got 0 results and 0 matches ----
# we got 0 results and 0 matches  

#cy.main('stress[0,250]test')
#Got 3374 results and 7355 matches
# we got 3377 results and 7350 matches

#cy.main('object[10, 200]application[0, 100]python[10, 200]system[0, 100]computer[0, 10]science[0, 150]linux[0, 200]ruby') 
#Got 1 results and 1 matches
# Got 1 results and 1 matches  ------

# ------ Extra ------

# Test with answers
#cy.main('elephants[0,20]are[0,20]to')

# Google
#cy.main('cat[0,10]are[0,10]to')
#cy.main('dog[0,10]anatomy')


#cy.main("big[0,20]data[0,20]query") ---
#cy.main("cat[0,10]are[0,10]to")
#cy.main("dogs[0,15]are[0,15]to")
#cy.main("hopefully[10,20]no[10,20]matches") ---
#cy.main("python[0,10]programming[0,10]language")
#cy.main("wikipedia[0,20]article")

