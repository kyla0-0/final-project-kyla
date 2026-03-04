define c = Character("Candi", color="#B20100")
define m = Character('Me', color="#084747ff")


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

        c "That’s nice! Or not, depending on whether you like them dead or alive…"

        jump contin1

    label nope:

        c "Like, personally? If so, I have some good news for you…"

        jump contin1

    label contin1:
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

    return