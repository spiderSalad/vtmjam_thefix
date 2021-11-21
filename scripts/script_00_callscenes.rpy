init 2 python:
    import random

label index:

    label .hunts:

        define sadman   = Character("Stressed Man", color = "#fefefe")
        define robber   = Character("Stick Up Kid", color = "#fefefe")
        define raver    = Character("Clubgoing Woman", color = "#fefefe")

        label .establish_orientation:
            menu
                "I'm looking for..."

                "Men.":
                    $ story_orientation = SIREN_MEN

                "Women."
                    $ story_orientation = SIREN_WOMEN

                "Whoever catches my eye."
                    python:
                        story_orientation = SIREN_BOTH
                        story_this_time = SIREN_WOMEN if random.randInt(0, 1) > 0 else SIREN_MEN
            return

        label .hunt1_consensualist:

            scene bg image bg hunt1 consensualist

            if not MUSIC_MUTED:
                play music audio.consensualist fadein 0.5

            "There's an art and a science to getting a human being to voluntarily let you drink their blood. It's all about knowing your audience."

            me "All that, {i}and{/i} you're taking night classes? Don't get me wrong man, I respect the hustle. No doubt. But what about her? Is she not able to work?"

            sadman "She's dealing with some pretty severe mental health issues. Gotta step up and be there for her, y'know?"

            me "But you gotta take care of yourself too. Your lives are in transition. You don't want to burn out in transition, trust me."

            menu:
                me "Because..."

                "\"Prolonged stress can break down your body, same as physical injury. You only get one body, you gotta protect it.\"":
                    $ pc.addDisciplinePower(_fortitude, FORT_HP)

                "\"All that stress will make you crack, dude. Break your will. You've got to protect your mental health.\"":
                    $ pc.addDisciplinePower(_fortitude, FORT_STUBBORN)

            sadman "I'm doing what I can, but I don't have a whole lot of options. Most people don't these days. Gotta tough it out, right?"

            me "You ever think about therapy?"

            sadman "For as long as it takes me to remember I ain't got health insurance."

            "I give him a sympathetic wince and pat him on the shoulder."

            me "It's rough out here, huh? Seems like everyone's struggling."

            sadman "Yeah. Hey, thanks for listening. I gotta get going."

            me "Sure man, good luck out there. Hey, have you ever...? Nevermind."

            sadman "Hm?"

            me "I just thought... Okay, you gotta promise not to laugh."

            sadman "Not too much is funny these days."

            me "It's just, it's kinda weird. I almost don't even want to bring it up, but I'd feel bad if I didn't. 'Cause it {i}really{/i} helped me."

            sadman "What are you talking about? What helped?"

            me "It's kinda this New Age thing, balancing out chakras and all that. Stuff you've probably tried before. But this one actually works, I swear to God. You a spiritual guy?"

            sadman "I like to think there's more to this universe than we've figured out."

            me "Right on. So you've heard about how leeching used to be considered this barbaric, medieval practice, right? But then science discovered that there are totally legitimate medical uses for a leech. You follow me?"

            sadman "Yeah, I heard about that. I think there's a lot of wisdom to be found in, like, old traditions and stuff. Wise women, traditional Chinese medicine, folk remedies and all that. Even if it's not all literally true."

            me "Exactly! You get it, man! So it's kinda like that. It's exactly like that, actually. You'll notice the effects right away."

            sadman "Wait, what?"

            me "Yeah, all that pent up stress is building up in your chi, like plaque or something. But there's a way to release it."

            sadman "And it involves... drinking my blood?"

            me "Haha, yeah. Like, you can't just cut yourself; you need a partner to draw out the bad chi with the blood. Hey man, if it's too weird for you, I get it. I only brought it up 'cause it did wonders for me. No worries."

            "I make like I'm about to leave."

            sadman "...Honestly, I'm willing to try anything at this point. You were right. I am kinda burning out."

            "Got him."

            me "You sure? ...Okay. You want to step out this way?"

            "Once we're alone in shadow, and I'm sure there are no cameras, I hold up his arm."

            me "So it works like this-"

            play sound audio.bite1

            "And I bite. My fangs sink right into his wrist. Like they've always belonged there."

            queue sound audio.drinking1

            sadman "Ouch! Hey, what are- ...Oh. Oh shit..."

            "This is the closest thing to informed consent that I can safely get. I can't tell him what I am, but I can make him understand what I want to do, and then it's his choice. The lies are an unfortunate necessity."

            "But that's the funny thing - most of that bullshit I was feeding this poor guy is actually true, or at least in the same ballpark as truth. When we bite into a human and feed, it overwhelms them with pleasure."

            "For some it's like an orgasm; for others it's serene bliss. I know from experience how good this guy's feeling right now. So good that he'd probably let me keep drinking until he died. Until the last of his life flowed into me..."

            "But I only take what I need. And I wasn't totally lying about the other part, either. I can literally taste how much life has taken out of him. His battered ego, his eroded will. I drink in his despair and let it fill me."

            $ global pc
            $ pc.setHunger("-2")

            stop sound fadeout 0.5

            "And then I stop, and lick the wound away while he's still dazed."

            me "...How's that feel? Better?"

            sadman "...Huh? Oh. Oh, wow. That was... how did you do that?"

            "I want to let him have this, but duty calls. I will the raw life I just stole from him up through my veins until it's percolating behind my eyes."

            me "Don't worry, man. Just forget about it."

            "And with that, my mind reaches out to his and wipes the chalkboard clean. The last ten minutes or so, gone from his memory."

            me "Hey man, wake up! Jesus Christ man, you passed out! Do you need some water?"

            sadman "...What? Jeez, where-"

            me "You weren't kidding about the stress, man. I had to pull you off the sidewalk. Do you need to go to the hospital?"

            "At the mention of hospitals a bit of his worries return. Sorry, buddy. He shakes his head."

            sadman "Nah, nah I'm good. It was nice meeting you, uh..."

            me "Michelle."

            sadman "Take care of yourself, Michelle."

            me "You too."

            "And that's that. I watch him leave, then head back towards the parking garage off Hendrix."

            $ pc.removeFromInventory("cash", 50.0)

            return

        label .hunt1_roadsidekiller:

            scene bg hunt1 roadsidekiller

            if not MUSIC_MUTED:
                play music audio.roadside_killer2 fadein 0.5

            "Gas stations are like the lymph nodes of a city. Liminal spaces where millions of lives intersect in a way you don't see in most other places. No matter your walk of life, everybody's got somewhere to be. Something to take with them, something to drop off."

            "To flee from something is to move, literally or figuratively. It's only logical then, to hunt amidst a hub of human movement. Half the people here are probably running from something."

            "Speaking of which..."

            robber "Good evening~ Ma'am."

            "He says it in a mocking drawl and flashes his .22. We're in a lot behind the gas station. It's barely lit."

            robber "How {i}are{/i} we doing this fine evening?"

            "I give him my best smile. I can't even tell how old this guy is. His voice is deep and rumbling, but he's short and babyfaced."

            me "Better now."

            robber "Oh, I'm {i}very{/i} glad to hear it. So nice to see some support for the youth out here. Then let us not waste {i}any{/i} more time under this fine evening sky."

            "The thing about these stick up kids - they're always on the move. Always on the run from something."

            robber "I'll be happy to accept your donation in the form of that purse and that {i}lovely{/i} silver locket. That's real silver, ain't it Ma'am?"

            beast "We're gonna eat this little shit, right? As opposed to your usual routine of gingerly nibbling and then prancing away? Because I'd love an actual meal and this little stray seems perfect."

            me "Yep. So what do you need the money for? Everything okay?"

            "His mocking smile gets wider."

            robber "Oh you are {i}so{/i} kind to ask after my home life, Miss. I'm doing just fine. But I really must {i}insist{/i} we hurry this transaction along."

            "He raises the gun."

            me "I didn't say anything about your home life. Is that why you're doing this? An abusive home? Or none at all?"

            "His smile disappears and he levels the gun at my chest."

            robber "I ain't gonna {i}ask{/i} you again, Ma'am."

            menu:
                beast "He's pointing a gun at us, he's fair game! Fucking drain him!"

                "Please. I don't crack that easily. This kid doesn't scare me, and neither do you. I look him straight in the eye and continue on as if I didn't even hear him.":
                    $ pc.addDisciplinePower(_fortitude, FORT_STUBBORN)

                    me "Tell me what you really need. I can help you a lot more than fifty bucks and some fake jewelry will."

                    robber "I need you to shut the fuck up and run me that goddamn-"

                    me "What's the hurry? You got a fuckin' curfew? Is your momma gonna whoop your ass if you're out too late jacking people up?"

                    robber "...Nah, fuck this."

                    "His finger tightens on the trigger."

                    beast "If he shoots us the noise will draw people over. Someone will call the cops. We won't have enough time to feed! Goddamnit, drain the little puke. We already knew he's a fucking stray."

                    me "You don't want to go home, do you? It's the shelter that has the curfew. If you aren't back soon they'll lock their doors and you'll be out on the cold streets."

                    "He gapes at me with open loathing, like he can't believe what he's hearing. There it is. He starts to raise the gun from my chest to my head."

                "It'd take a lot more than that pea shooter to bring me down, and I tell the kid as much.":
                    $ pc.addDisciplinePower(_fortitude, FORT_HP)

                    me "You're not scaring anybody with that toy, Fisher Price. Why don't you tell me what you really want? Thirty bucks, fake jewelry and some cards I'm just gonna cancel ain't gonna help nearly as much as you seem to think."

                    robber "The audacity of this bitch. If you don't run me that motherfuckin' purse-"

                    "He keeps sneaking glances in the other direction. I step closer, my arms wide."

                    robber "Back the fuck up!"

                    me "You got somewhere to be, huh? Where do you stay, anyway?"

                    "His right eye twitches for a split second. I've got him."

            robber "Motherfuck-"

            play sound audio.tackle1

            "I pounce, bowling him over and closing my fist around the slide of his gun. He spits curses, tries to fire with one hand and punch me with the other. But my fangs are in him already and a half second later he goes limp."

            queue sound audio.bite1

            queue sound audio.drinking1

            "They're usually helpless once we bite. I ignore his groans and sighs and resist the temptation to drink faster. Feeding too quickly can cause a lot of harm."

            beast "It's a perfectly natural urge. Stop resisting it."

            "I wonder where this kid thought he was going. His fear and rage flow into my veins until I feel like gnawing through his windpipe and gouging out his eyes."

            beast "I like where your head's at."

            "No. I stop when I have what I need, and lick the wound closed. His breathing is a bit shallow, but it's steady. Christ, he looks really young lying there like that. I can't leave him here."

            beast "{alt}Sigh{/alt}..."

            "But there's nowhere to take him. Not that I can get to quickly. I stuff a bit of cash into his pocket so he can at least buy something to eat when he comes to."

            $ pc.removeFromInventory("cash", 100.00)

            return

        label .hunt1_scenequeen:

            scene bg hunt1 scenequeen

            if not MUSIC_MUTED:
                play music audio.scene_queen fadein 0.5

            "Deafening beats pounding like God's own heart. Fog machine spreading white haze everywhere. Looks like half the people here are rolling or drunk."

            "I'm home."

            $ pc.removeFromInventory("cash", 70.00)

            "I wish I could partake, but if I drink from any of the molly poppers in the crowd I'll be sitting next to them on that flight. Showing up late is already pushing it; I can't show up to work high. Especially now that my bosses ares vampires."

            beast "Let's hit the dance floor. We can scan the rest of the place for prey, and if we're lucky it'll come to us."

            "Now you're speaking my language."

            "I proudly take my place amid the press of writhing, twisting, jerking bodies. I roll my hips and sway my shoulders to the thumping beat. My dress is getting soaked with other people's sweat, but I don't care. Dancing here, I'm almost alive again."

            beast "Look! Over there, in the bright red tube top."

            "I'm looking. She glances my way for an instant, smiles, and goes back to wining, tracing patterns on the floor with her shoes. She's slightly off beat, but she's having a great time and I'm here for it. I shuffle and sway my way over."

            "She gives me a look and steps closer, still dancing. She looks older than me, but you never know. She's rocking one of those short side-swept cuts. I don't know if she's my type yet, but I have a good feeling."

            "She puts her hands on my hips and I let her pull me into an intimate dance, our hips swaying in sync and our legs almost intertwining. That's not what I came for, but attraction never hurts when you're hunting. So I indulge her for a bit."

            menu:
                "But only for a bit. I look into her eyes and my Blood surges up into my lips and tongue. I say to her..."

                "\"Come with me.\" A quick, concise command will let me get her out of the crowd and into a nearby alcove with minimal effort. Don't want to be any more late than needed.":
                    $ pc.addDisciplinePower(_dominate, DOM_COMPEL)

                    "A lot of Blue Bloods wield this power like a bludgeon, trying to crush their victim's will. But it doesn't have to be. Sometimes someone is already inclined to do something, and the best thing to do is to just... guide them along."

                    "To save time, and make sure nothing goes awry."

                    "This power doesn't work if they don't hear you, so I make sure can hear me. Despite the thundering beats and wailing synths. Despite all the noise of the crowd."

                    $ pc.addPerk(M_LINE_HARDESTADT, 1, merit = True)

                    if story_background == "defender":
                        "It's like the ambush, back when I was mortal. My sire shouted and I heard every word, no matter how loud everything else got. Maybe I inherited it from her?"
                    else:
                        "It's a weird thing I can do. I don't think it's the same as the normal Ventrue arts, but I haven't had time to look into it."

                    "We're at a table far from the dance floor proper, in shadow one moment and blinding strob the next. I take off my locket and show it to her."

                "\"You seem really nice! Wait for me upstairs, at that table near the back. I'll get us some drinks and we'll get to know each other.\" It'll take more juice, but a more powerful and complex command makes it a lot less likely that anything will go wrong.":
                    $ pc.addDisciplinePower(_dominate, DOM_MESMERIZE)
                    $ pc.setHunger("+1")

                    "It's important to word these longer commands carefully. There are a lot of faux pas you can make that will just confuse your prey, or make them behave in unpredictable ways. Plus, they take more out of me than the memory thing."

                    "But this should work. Mesmerism will get her up the stairs and into the shadows, and a combination of actual interest and ingrained politeness will keep her there."

                    "I wonder if she noticed, if it occured to her how weird it is that she could hear me just fine over all this noise. I made sure she could, because the power doesn't work if they don't."

                    $ pc.addPerk(M_LINE_HARDESTADT, 1, merit = True)

                    if story_background == "defender":
                        "It's like the ambush, back when I was mortal. My sire shouted and I heard every word, no matter how loud everything else got. Maybe I inherited it from her?"
                    else:
                        "It's a weird thing I can do. I don't think it's the same as the normal Ventrue arts, but I haven't had time to look into it."

                    "I go and get us a pair of Mai Tais, only one of which is likely to get drank. Unfortunately. Regular food and drink just comes right back up unless I force it to stay down, and even then it's just a matter of time."

                    "There's a lot Kindred just can't do. Sometimes being undead is a shit deal. But hopefully that's about to change."

                    "When we get to our booth in the back I take off my locket and hand it to her."

            raver "It's beautiful. Is it real?"

            me "Yeah. My Lola gave it to me."

            raver "Lola? Is she, like, your ex?"

            "I suddenly notice the fading imprint around her ring finger. It's a gamble, but that might be my angle."

            me "{alt}Laughing: {/alt}No, no. My {i}grandmother{/i}."

            raver "Oh, that's cool."

            me "We're from Hawaii originally. Lola gave it to me to me when I came out here to get away from where it all fell apart. You want to put it on?"

            raver "Huh? Oh, sure. You said... where it all fell apart... Are you okay?"

            me "I am now, yeah. Thanks for asking. That looks beautiful on you, by the way. I think that's why a lot of people end up in this city."

            raver "...Because your necklace looks good on me?"

            "I giggle at her like she just told a joke. Her face is lit with alternating pink and blue strobes."

            me "No, I think a lot of people are like me. They come here to get away from something. Or someone. I don't necessarily mean, like, physical danger. Sometimes you can't stay because it just hurts too much, you know?"

            raver "...Yeah, I guess I do."

            "I touch her hand, and she intertwines her fingers with mine without taking her eyes off me once."

            me: "Are you like that?"

            raver: "What do you mean?"

            me: "Here because it hurts too much to be back there."

            raver: "I don't really want to think about tha-"

            play sound audio.bite1

            "It'll do. I bite."

            queue sound audio.drinking1

            "She gasps, then sighs in pleasure and starts to run her hands through my hair."

            beast "You worked pretty hard for this one, huh? I think you deserve a treat."

            "I do let myself enjoy the flavor. Sadness, betrayal, lust, longings bitter and hopeful... But I don't let myself take enough to hurt her. Not permanently, anyway. I unclasp my locket and take it off of her. Then I stop feeding."

            $ pc.setHunger("-2")

            raven "That was... what {i}was{/i} that?"

            me: "Don't worry. Forget about it."

            "She blinks and then her eyes glaze over. I want to head back to the dance floor, but I've taken up enough time."

            return

        label .hunt1_siren:
            call index.hunts.establish_orientation from hunt_start_early_siren

            if story_this_time == SIREN_WOMEN:
                scene bg hunt1 siren_women with fade
                jump index.hunts.hunt1_siren.drinkwomen
            else
                scene bg hunt1 siren_men with fade
                jump index.hunts.hunt1_siren.drinkmen

            label .drinkmen:
                "yeaaah men"
                return

            label .drinkwomen:
                "eaaah women"
                return
