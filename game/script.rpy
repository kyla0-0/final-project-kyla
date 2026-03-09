define c = Character('Candi', color="#B20100")
define m = Character('Me', color="#084747ff")
define g = Character('Gus', color="#ABGG24")
image candi = "defcan.png"
image candi surprised = "supcan.png"
image bg townent = "townEntrance.png"


label start:

    scene bg town
    with fade

    "I've finally arrived..."

    "Salmontin. Population: 200. I wonder what this town's like."

    "Smells like salmon. Not like too much like tin, though."

    "The only thing reminiscent of tin here is me."

    "Yep. Me, a human named Tin. My parents make tin for a living."

    "I'm expecting to meet people in this town named 'Fish.'"

    show candi
    with moveinright

    c "...Tin? Hey hey hey, Tin! You're here pretty early."

    m "Haha, yep! I'm kinda surprised too."

    c "Welcome to Salmontin, Tin! Hehe…"

    c "This is a great town, I'm glad you decided to move here!"

    c "And I'm also glad that you decided to become a fisher."

    c "Fishing life… It's something else."

    c "Do you like fish?"

    menu:
        "Yeah":
            jump yeah

        "Nope":
            jump nope

    label yeah:

        c "That's nice! Or not, depending on whether you like them dead or alive…"

        jump contin1

    label nope:

        show candi surprised

        c "Like, personally? If so, I have some good news for you…"

        jump contin1

    label contin1:

        show candi -surprised
            
        c "Y'know, I like fish both as an animal and as a dish. Speaking of fish..."

        c "I know you just got here, but we should fish now before it gets dark. It's best you learn how to fish as soon as possible."

        m "What's with the rush? Can't I get situated first? In my house?"

        c "The movers are still getting things ready. You were supposed to arrive tomorrow morning."

        c "Follow me, I'll carry your bags for you. I have some more supplies for you in my boat."

        scene bg cboat
        with fade

        c "Welcome aboard matey! My grand galleon!"

        m "...A galleon?"

        c "It's a type of ship...Like the one pirates have..You don't follow pirate lore?"

        m "?"

        c "...Moving on. There aren't many pirates around these waters anyway."

        c "This is a cast net. The part I'm holding here is called a handline."

        c "So what you do is hold one end of the handline with both hands and then throw the net into the water in a circular motion."

        c "The net has weights around it so it'll sink. Keep at tight grip so you don't drop the net."

        c "Now you try!"

        c "See? Easy. Now we wait."

        c "In the meanwhile, I'll tell ya about responsible fishing practices. There's all types of rules and guidelines you have to follow."

        c "First of all, you should only fish in areas where you're allowed to."
        
        c "There will be areas where there's a sign that says fishing is prohibited. Don't go in those prohibited areas."

        c "They're prohibited for a reason! Fish populations need time to replenish, and there's also endangered species in those areas."

        c "Another rule among fishers! Don't fish more than the daily limit."

        c "Only catch as much fish as you can fit in one boat trip. That way the fish populations stay in check."

        c "And as a fisher, try your best to only catch fish. No sharks, turtles, or any of the like. And don't cause environmental damage."

        c "To do this, you need to use the right fishing methods. Don't use bottom trawls. Bottom trawls are nets dragged across the sea floor. Very destructive!"

        c "And don't use dynamite???? That is really illegal. But I've seen it happen, unfortunately. The perpetrator got executed."

        c "Best to stick with the methods I show you."

        c "Oh, and one last rule. Don't work for big fisheries! You're plenty fine on your own."

        m "What are fisheries?"

        c "They're basically fishing businesses. A lot of 'em just care about profit, and only profit. The work is very physically taxing."

        "Some time later..."

        c "Ok, the nets are full. Now pull your net in."

        c "Any questions so far?"

        m "I'm hungry"

        c "Ok, that'll be it for today."

        c "Let's stop by your house to see if it's done."

        scene mhouse
        with fade

        "Some time later..."

        c "Seems like the movers just finished up. That's good."

        c "Well, see ya later, alligator!"

        m "See ya!"

        hide candi

        m "Home sweet home..."

        m "Looks just like my old home, just with a different floor plan."

        m "How did they know what my old home looked like?"

        m "Let's see if there's anything in the fridge."

        "The next day: Morning"

        m "Yawwwwn"

        m "...Who is that at the door?"

        show gus

        g "HAIIIIIIIIIIIIIII! My name's Gus and I'm your neighbor!!"

        g "Welcome to Salmontin, Tin! (hahaha, tin tin...)"

        m "(Is everyone gonna say this?)"

        g "The town is very excited to get to know you! We've heard a bit about you already and you seem great!"

        g "If you ever need a fishing buddy, I'd be stoked to be one!"

        m "One more fishing buddy couldn't hurt."

        g "You have one already? Who is...Oh. Candi, right?"

        m "Yep."

        g "Haha, I know her! She's like one of the best fishers in town."

        g "Y'know, you might hear some rumors about her, but I wouldn't pay them any mind. A lot of people think she's evil, but she's actually really sweet."

        g "I can't say too much about this, so don't ask."

        m "(I was gonna ask...)"

        g "Speaking of people you should stay away from, stay away from Fish. He's going to destroy this town with the way he fishes!"

        g "He's so bad that it's like he's singlehandedly contributing to the GLOBAL problem of overfishing!"

        m "(A guy named Fish is a bad fisher??)"

        g "If it's alright with you, we could go on a little fishing trip today. After you get ready, of course!"

        g "The mayor is still working on getting you a boat, so in the meantime, you'll have to fish with all of us!"

        m "Sure."

        g "Yayy!! See you later."

        scene gboat
        with fade

        "Later..."

        g "You're a beginner, right? So we'll start off with fishing rods! They're a classic."

        g "They're not very efficient for commercial fishing, but you still need to know how to use them efficiently."

        g "We use them for town fishing competitions, and the winners get a trophy!"

        g "First, we attach the bait to the hook. Then we cast the rod into the water and wait."

        g "When you feel a tug, reel it in!"

        g "Any questions in the meantime? And only questions about fishing and the like, please."

        menu:
        "The rumors about Candi?":
            jump rumor1

        "Good fishing methods?":
            jump fishmethod1

        "What does overfishing do?"
            jump over1

        label rumor1:
            
            g "As I said, I can't talk about that..."

            g "And double as I said, only fishing questions..You got any fishing questions?"

            menu:

                "Good fishing methods?":
                    jump fishmethod1

                "What does overfishing do?"
                    jump over1

        label fishmethod 1:

            g "Good question!"

            g "You should use LED nets. They're great for targeting specific species since different LED colors attract different species."

            g "They're also great at reducing bycatch! Bycatch is when marine animals are unintentionally captured while trying to catch other marine animals."

        label over1:
            g "It depletes the population of marine species faster than they can reproduce. Messes up the whole ecosystem."

            g "Makes fishing harder for everyone. People can't get the fish they want and fishers struggle to make money."

            g "Many people had to leave this town because they couldn't make enough to support their family."

            g ""

























    return