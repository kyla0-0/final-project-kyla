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

    return