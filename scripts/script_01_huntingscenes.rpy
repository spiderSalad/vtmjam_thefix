init 2 python:
    import random

    pcname = _pc["first"]
    pclast = _pc["last"]
    petname = _pc["pet"]
    ghoulname = _pcGhoul["first"]
    ghoulpet = _pcGhoul["pet"]

label feeding:

    define sadman   = Character("Stressed Man", color = "#86edeb")
    define robber   = Character("Stick Up Kid", color = "#99cc68")
    define raver    = Character("Clubgoing Woman", color = "#e68044")
    define cuteman  = Character("Dancing Man", color = "#e378ba")
    define lloyd    = Character("Lloyd", color = "#e378ba")
    define cutelady = Character("Selfie Taker", color = "#e378ba")
    define ang      = Character("Ang", color = "#e378ba")

    define escort   = Character("Escort", color = "#86edeb")
    define kinkster = Character("Autohaemofetishist", color = "#86edeb")
    define someguy  = Character("Solitary Motorist", color = "#99cc68")
    define carlady  = Character("Tourist in Truck", color = "#99cc68")
    define edmlady  = Character("Impressed Dancer", color = "#e68044")
    define hollowman= Character("Gaunt Man", color = "#e68044")
    define cuteman2 = Character("Beautiful Man", color = "#e378ba")
    define cutelady2= Character("Beautiful Woman", color = "#e378ba")

    label .establish_orientation:

        $ global pcex

        menu:
            "I'm looking for..."

            "Men.":
                $ story_orientation = SIREN_MEN
                $ story_this_time = SIREN_MEN
                $ pcex = _exmale

            "Women.":
                $ story_orientation = SIREN_WOMEN
                $ story_this_time = SIREN_WOMEN
                $ pcex = _exfemale

            "Whoever catches my eye.":
                python:
                    story_orientation = SIREN_BOTH
                    if random.randint(0, 1) > 0:
                        story_this_time = SIREN_WOMEN
                        pcex = _exmale
                    else:
                        story_this_time = SIREN_MEN
                        pcex = _exfemale

        $ story_orientation_set = True

        return

    label .hunt1_preamble:

        "My type is... hard to explain. I had a hell of a time figuring it out myself. Basically I feed on people who are, well, in flight. People running from something. Trying to put something behind them."

        "What exactly it is doesn't matter per se. It can be a place, a person, an event, a state of mind. But they have to have physically moved somewhere in order to get away from it, and - this is the killer - they have to let me know about it."

        "They don't have to do it intentionally, or even verbally. Sometimes just a furtive or pained look on their face is enough. But there has to be a tell. I have to {i}know.{/i}"

        beast "You are what you eat, or rather you eat what you are. Cowards running from their problems. You're a spiritual cannibal, feeding on those like yourself."

        stop music fadeout 2.0

        play sound audio.carstopengine_pc

        "...You finished, Socrates? Because here we are."

        queue sound audio.carstopkeys_pc

        queue sound audio.heels_on_pavement

        scene black with fade

        "Naturally I don't park where I plan to hunt. (Not that I could, even if I wanted to.) I park a few blocks out and hoof it the rest of the way."

        return

    label .hunt1_consensualist:

        scene bg hunt1 consensualist

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
                $ pc.setPredatorTypePower(_fortitude, FORT_HP)

            "\"All that stress will make you crack, dude. Break your will. You've got to protect your mental health.\"":
                $ pc.addDisciplinePower(_fortitude, FORT_STUBBORN)
                $ pc.setPredatorTypePower(_fortitude, FORT_STUBBORN)

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

        $ pc.soundFeed("And I bite. My fangs sink right into his wrist. Like they've always belonged there.")

        sadman "Ouch! Hey, what are- ...Oh. Oh shit..."

        "This is the closest thing to informed consent that I can safely get. I can't tell him what I am, but I can make him understand what I want to do, and then it's his choice. The lies are an unfortunate necessity."

        "But that's the funny thing - most of that bullshit I was feeding this poor guy is actually true, or at least in the same ballpark as truth. When we bite into a human and feed, it overwhelms them with pleasure."

        "For some it's like an orgasm; for others it's serene bliss. I know from experience how good this guy's feeling right now. So good that he'd probably let me keep drinking until he died. Until the last of his life flowed into me..."

        "But I only take what I need. And I wasn't totally lying about the other part, either. I can literally taste how much life has taken out of him. His battered ego, his eroded will. I drink in his despair and let it fill me."

        $ global pc
        $ pc.slakeHunger(2)

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

        $ pc.loseCash(50.0)

        scene black with fade

        return

    label .hunt1_roadsidekiller:

        scene bg hunt1 roadsidekiller

        if not MUSIC_MUTED:
            play music audio.roadside_killer fadein 0.5

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
                $ pc.setPredatorTypePower(_fortitude, FORT_STUBBORN)

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
                $ pc.setPredatorTypePower(_fortitude, FORT_HP)

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

        $ pc.slakeHunger(2)
        $ pc.loseCash(100.00)

        scene black with fade

        return

    label .hunt1_scenequeen:

        scene bg hunt1 scenequeen

        if not MUSIC_MUTED:
            play music audio.scene_queen fadein 0.5

        "Deafening beats pounding like God's own heart. Fog machine spreading white haze everywhere. Looks like half the people here are rolling or drunk."

        "I'm home."

        $ pc.loseCash(70.00)

        "I wish I could partake, but if I drink from any of the molly poppers in the crowd I'll be sitting next to them on that flight. Showing up late is already pushing it; I can't show up to work high. Especially now that my bosses are vampires."

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
                $ pc.setPredatorTypePower(_dominate, DOM_COMPEL)

                "A lot of Blue Bloods wield this power like a bludgeon, trying to crush their victim's will. But it doesn't have to be. Sometimes someone is already inclined to do something, and the best thing to do is to just... guide them along."

                "To save time, and make sure nothing goes awry."

                "This power doesn't work if they don't hear you, so I make sure can hear me. Despite the thundering beats and wailing synths. Despite all the noise of the crowd."

                $ pc.addPerk(M_LINE_HARDESTADT[KEY_NAME], 1, merit = True)

                if story_background == "defender":
                    "It's like the ambush, back when I was mortal. My sire shouted and everyone heard every word, no matter how loud everything else got. Maybe I inherited it from her?"
                else:
                    "It's a weird thing I can do. I don't think it's the same as the normal Ventrue arts, but I haven't had time to look into it."

                "We're at a table far from the dance floor proper, in shadow one moment and blinding strob the next. I take off my locket and show it to her."

            "\"You seem really nice! Wait for me upstairs, at that table near the back. I'll get us some drinks and we'll get to know each other.\" It'll take more juice, but a more powerful and complex command makes it a lot less likely that anything will go wrong.":
                $ pc.addDisciplinePower(_dominate, DOM_MESMERIZE)
                $ pc.setPredatorTypePower(_dominate, DOM_MESMERIZE)
                $ pc.raiseHunger(1)

                "It's important to word these longer commands carefully. There are a lot of faux pas you can make that will just confuse your prey, or make them behave in unpredictable ways. Plus, they take more out of me than the memory thing."

                "But this should work. Mesmerism will get her up the stairs and into the shadows, and a combination of actual interest and ingrained politeness will keep her there."

                "I wonder if she noticed. If it occured to her how weird it is that she could hear me just fine over all this noise. I made sure she could, because the power doesn't work if they don't."

                $ pc.addPerk(M_LINE_HARDESTADT[KEY_NAME], 1, merit = True)

                if story_background == "defender":
                    "It's like the ambush, back when I was mortal. My sire shouted and everyone heard every word, no matter how loud everything else got. Maybe I inherited it from her?"
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

        "She doesn't need any help hearing me, but I do have to focus to make out what she's saying over the din."

        me "We're from Hawaii originally. Lola gave it to me to me when I came out here to get away from where it all fell apart. You want to put it on?"

        raver "Huh? Oh, sure. You said... where it all fell apart... Are you okay?"

        me "I am now, yeah. Thanks for asking. That looks beautiful on you, by the way. I think that's why a lot of people end up in this city."

        raver "...Because your necklace looks good on me?"

        "I giggle at her like she just told a joke. Her face is lit with alternating pink and blue strobes."

        me "No, I think a lot of people are like me. They come here to get away from something. Or someone. I don't necessarily mean, like, physical danger. Sometimes you can't stay because it just hurts too much, you know?"

        raver "...Yeah, I guess I do."

        "I touch her hand, and she intertwines her fingers with mine without taking her eyes off me once."

        me "Are you like that?"

        raver "What do you mean?"

        me "Here because it hurts too much to be back there."

        raver "I don't really want to think about tha-"

        $ pc.soundFeed("It'll do. I bite.")

        "She gasps, then sighs in pleasure and starts to run her hands through my hair."

        beast "You worked pretty hard for this one, huh? I think you deserve a treat."

        "I do let myself enjoy the flavor. Sadness, betrayal, lust, longings bitter and hopeful... But I don't let myself take enough to hurt her. Not permanently, anyway. I unclasp my locket and take it off of her. Then I stop feeding."

        $ pc.slakeHunger(2)

        raver "That was... what {i}was{/i} that?"

        me "Don't worry. Forget about it."

        "She blinks and then her eyes glaze over. I want to head back to the dance floor, but I've taken up enough time."

        scene black with fade

        return

    label .hunt1_siren:

        if not story_orientation_set:
            call feeding.establish_orientation from hunt_start_early_siren

        if story_this_time == SIREN_WOMEN:
            scene bg hunt1 siren_women with fade
            jump feeding.hunt1_siren_drinkwomen
        else:
            scene bg hunt1 siren_men with fade
            jump feeding.hunt1_siren_drinkmen

        label .hunt1_siren_drinkmen:

            play music audio.siren_men1 fadein 0.5

            $ pc.loseCash(50.0)

            "Not exactly my scene, but not bad. Place is hopping, and I can definitely dance to this."

            "I weave my way past the impromptu mosh and onto one of the other dance floors."

            beast "Look! Two o' clock."

            "And there he is, off in his own world. A cute guy with locs running down past his shoulders, doing some kind of krump to the beat."

            "I think I like this one. I like his hair. I like the way his shirt hangs off his muscles. I like the almost beatific expression on his pretty face as he dances his little heart out. But is he my type?"

            "Now, I could easily be wrong. Maybe he's just really feeling the music. Maybe he's rolling. Maybe he just likes to dance."

            "But in my experience, guys dancing alone like that are usually trying to get into a certain headspace. Or out of one. Like they're on a vision quest, or seeking some kind of spiritual epiphany."

            "Most people have things they'd like to forget, to figuratively leave behind. But maybe there's a literal component here. Or maybe I'm making a bunch of completely unfounded assumptions. But I have a good feeling."

            "Now, how best to approach? This dance floor isn't exactly packed, but there are a lot of people between us."

            menu:
                beast "Why waste time letting kine get in the way of our hunt? Invoke the power of our Ventrue Blood and be done with it."

                "What did I tell you about using slurs? But you're right, it's time to clear a path.":
                    $ pc.addDisciplinePower(_presence, PRES_DAUNT)
                    $ pc.setPredatorTypePower(_presence, PRES_DAUNT)

                    "My dead heart beats once. I feel it even over the thumping bass. Blood surges up to my face and diffuses throughout my body, just under the skin."

                    "Predatory dominance radiates off of me, and people who weren't paying attention suddenly start to notice me and give me a wide berth. Like I was eight feet tall and growling in their ears. \"Step the fuck back.\""

                    "Control is always a must, of course. I take care that the aura of dread I'm projecting passes by my prey. Don't want to drive him off. I make my way up to him and seamlessly transition into a basic two-step."

                "Don't call them that. But you're right. I'll use my allure to have him come to me.":
                    $ pc.addDisciplinePower(_presence, PRES_AWE)
                    $ pc.setPredatorTypePower(_presence, PRES_AWE)

                    "Not just the normal allure I had when I was alive, either. I may have a face like Gemma Chan, a voice like Ella Fitzgerald, and a body like-"

                    beast "{i}God in heaven{/i}, will you get on with it?"

                    "But all of those things require the prey to already be paying attention to me. Not this, though. My Blood percolates under my skin, behind my face, everywhere. Swirling throughout me, tracing the motion of my hips."

                    "Suddenly all eyes are on me, and all jaws hit the floor. {i}Goddamn right.{/i} Well, in the immediate vicinity, anyay. But I make sure my aura of grandeur is concrated on one man, and I {i}definitely{/i} have his attention now."

                    "We stare into each other's eyes for a moment, and I give him my best \"come hither\" smile. He makes his way over. His eyes are sad and red-rimmed, but the rest of his body language says something different."

            me "Hey there."

            "The sheen of sweat over his dark skin makes him shine like the Northern Lights when the strobes pass over him. He's gorgeous. I hope I'm right about him. I make sure he can hear me over the noise."

            $ pc.addPerk(M_LINE_HARDESTADT[KEY_NAME], 1, merit = True)

            if story_background == "defender":
                "It's like the ambush, back when I was mortal. My sire shouted and everyone heard every word, no matter how loud everything else got. I must have inherited it from her."
            else:
                "It's a weird thing I can do. I don't think it's the same as the normal Ventrue arts, but I haven't had time to look into it."

            cuteman "Hey. I don't think I've seen you around before..."

            me "Salome."

            cuteman "...Like in the Bible? That's crazy."

            "Unlike the other way around, I have to strain to hear him, but I force a bit of Blood into my ears and brain and I manage. Still don't get how that works, but it works."

            me "Probably not even the craziest thing you've heard this week."

            cuteman "True, true!{alt} He laughs.{/alt} Whole world's going crazy these days, huh? I'm Lloyd, by the way."

            "I lower my voice to a purr, and then I flush Blood throughout my body, forcing my dead flesh and organs to behave as if they're alive. Almost immediately I start to sweat. And then I step a bit closer in between figure-eights made with my hips."

            me "Pleased to meet you, Lloyd. Do you mean that in general, or do you mean {i}your{/i} whole world?"

            lloyd "...Now what would make you think something like that?"

            "I reach up to gingerly touch his face. He lets me."

            me "I could see the sadness in your eyes. They look a bit like mine."

            "He doesn't quite know what to say to that. After a moment he gives me a strange look."

            lloyd "I mean... Ain't everybody sad these days?"

            me "Maybe. But I come to places like this to get away from it all. What did you come here to get away from?"

            beast "Bit on the nose, don't you think?"

            lloyd "...Why don't we talk about something else?"

            me "Sure."

            "And I slide my arms under his. He puts his hands on my hips, and we dance for what feels like an hour. Pausing every once in a while to tell each other a joke or a story."

            "His breath is hot and minty. His scent is intoxicating, and it's not just the blood. I can't wait any longer."

            me "Do you want to get out of here?"

            lloyd "Yeah, I think I do."

            scene bg hunt siren_their_place with fade
            play music audio.siren_their_place fadeout 1.5 fadein 1.5 volume 0.8

            "I let him take me back to his place. It's small, spartan studio apartment on the fourth floor of the Huron-Farouk building. It's clean, almost immaculate. But it's got a hint of that wonderful lived-in smell."

            "We only make it to the bed because it looks so much comfier than the sofa. He kisses me long and deep, and then works his way down with his hands and lips while I fumble with his belt."

            "And he keeps working his way down, until... Oh. It's... good. Would probably be great if I were still alive. But it's time to move this show along, so I pull him up to his knees, kiss him, then shove him onto his back."

            "Once his shirt is off I take a moment to look him over. He's athletic and slender, with a visible inguinal crease and a couple of sexy scars across his chest. A total snack. I straddle him and bite. He shudders, moans, and jerks. I drink deep."

            $ pc.soundFeed()

            beast "Finally."

            "His love flows into me. It's strong and deep and only tinged at the surface with his lust for me. But underneath, at the core, there's a twisted knot of sour rage and bitter grief, like a worm in tequila. It's wonderful."

            "But now his heart is starting to flutter, and I can feel his blood pressure dropping in more ways than one. I'd better stop now."

            beast "You'd better not! We're almost there!"

            "Not today, you vile little shit. Not today. I kiss his neck one more time and the puncture wounds disappear. His breathing is shallow, but steady. He'll be okay. I think. I lean down and check his pulse. It's strong. Good."

            $ pc.slakeHunger(2)

            "I take one final moment to breathe in his scent again. It's mingled with mine, since I used the Blush of Life. I wonder who they were. The person he was mourning. Or who they are. The people we grieve for aren't always dead."

            beast "And now you've disappointed two people in one night. Usually you only manage one."

            "You're not a person; you're a skidmark on my soul. Besides, I'm pretty sure Lloyd got what he wanted. Shit, where'd I throw my underwear?"

            beast "I'm the only part of you that isn't delusional. I'm also the least disgusting part. A majestic tiger, caged amidst the circus of chattering, shit-flinging monkeys that comprises the rest of you."

            "Ignoring the \"tiger\", I wiggle back into my dress, smooth it a bit, grab my purse and excuse myself. I make sure to lock the door behind me. Goodbye, Lloyd. Thank you for sharing with me. I hope there are better days for you ahead."

            beast "Gag me with fucking spoon."

            $ pc.loseCash(20.0)

            scene black with fade

            return

        label .hunt1_siren_drinkwomen:

            play music audio.siren_women1 fadein 0.5

            $ pc.loseCash(50.0)

            "Not exactly my scene, but not bad. Place is hopping, and I can definitely dance to this."

            "I weave my way past the impromptu mosh and onto one of the other dance floors. I can feel the bass in my bones."

            "But no one's catching my eye. Oh, there are a ton of pretty girls here. Talking, drinking, texting, dancing, cheering, snapping pics with their phones. One woman in a cute emerald minidress is typing away on a MacBook."

            "Odd place to get writing done. More importantly, no one stands out to me as my type. Looks like I've got to canvas the place a bit."

            "..."

            "..."

            "It's been an hour of working my way around, chatting people up, dancing. A few groups want to take photos with me, which is understandable. I am kind of ridiculously hot."

            beast "Not this again..."

            "Face like Gemma Chan, voice like Ella Fitzgerald, body like-"

            beast "Focus!"

            "It's also not technically a Masquerade breach. A lot of us younger licks retain our human identities, because it's simpler and safer. But it's not the greatest thing for us to appear on social media."

            "Shit, I'm not getting anywhere. This hunt might just be a bust."

            beast "No! We are {i}not{/i} leaving hungry. Get back to work, unless you want {i}me{/i} to take over."

            "And with that threat, the searing, cloying ache of Hunger forces its way back to the front of my consciousness. I nearly double over. Alright, alright, Jesus! Let's switch tactics, then. We'll make another round, and see who looks {i}our{/i} way."

            beast "We are of the Clan of Kings. Crowds of kine are supposed to be putty in our hands! Use the power of our Blood."

            menu:
                "Fine, fine. I will my dead heart to beat, and it sends Blood throughout me, pooling and percolating just beneath my skin. Power radiates off me, power that-"

                "Draws the rapt gaze of the crowds closest to me. I'll scan my adoring public for anyone who looks suitable and suitably interested.":
                    $ pc.addDisciplinePower(_presence, PRES_AWE)
                    $ pc.setPredatorTypePower(_presence, PRES_AWE)

                    "I saunter through the crowd, trailing stares of awe and longing like the train of a wedding dress. But I'm looking for horny, not awestruck, and most of that is coming from men. The few women who look physically interested don't seem like my type."

                    "But wait, we might have something here. Across the way there's a pretty young Asian woman who was taking selfies with her friends until I got close. She absentmindedly lowers her phone, and I can feel her eyes all over me."

                    "Now we might be getting somewhere. I give her a wink and a smile and sashay my way over to the nearest booth. She turns back to her friends, who are snickering and ribbing her, goading her on. She pockets her phone and walks over."

                    cutelady "Hey. You, uh, come here often?"

                    "{i}Really?{/i} I raise an eyebrow at that. But I'm still smiling. I'm also running Blood throughout my system, forcing dead tissue to behave as if it's alive. She giggles, and I break out into a grin. She has to shout to be heard."

                    cutelady "I'm sorry, that sucked. Let's start over. Hi, I'm Ang."

                    $ pc.addPerk(M_LINE_HARDESTADT[KEY_NAME], 1, merit = True)

                    if story_background == "defender":
                        "Fortunately, I don't. It's like the ambush, back when I was mortal. My sire shouted and I heard every word, no matter how loud everything else got. I must have inherited it from her."
                    else:
                        "Fortunately, I don't. It's a weird thing I can do. I don't think it's the same as the normal Ventrue arts, but I haven't had time to look into it."

                    me "Mindy. Don't worry, I forgive you. And no, I just arrived the city a week ago. What about you?"

                    ang "Oh, I just come here to blow off steam. Get away from classes and sports and all that."

                    "Praise the Lord, we might just have our winner."

                    me "Get away from the pressure, you mean? I feel that."

                    ang "Yeah, exactly. You here on vacation, or...?"

                    me "I travel for work."

                    "And I spin a whole-ass yarn about how I write for a travel blog with an emphasis on city night life and the local subcultures around it. The blog is actually real."

                "Intimidates and unsettles those nearby, making them retreat from my presence without even knowing why. I'll sift through the crowd this way and keep an eye out for unusual levels of persistent interest... or fear.":
                    $ pc.addDisciplinePower(_presence, PRES_DAUNT)
                    $ pc.setPredatorTypePower(_presence, PRES_DAUNT)

                    "I stalk through the crowd. Big and small, soft and hard, they all shrink back. When I've passed out of range they give each other dumbfounded looks, like they're not sure what just happened. All except..."

                    "Across the way there's a pretty young Asian woman who was taking selfies with her friends until I got close. The other two women step back, suddenly terrified with no idea why. But not her."

                    "She stares at me with a mixture of fear, confusion, and fascination. But she doesn't shrink away. I focus my aura away from her, and onto her two friends. They flinch."

                    "I give them a wolfish smile that doesn't reach my eyes, and ask if I can talk to their friend for a bit. They don't waste any time excusing themselves. Wow. Some friends they are."

                    beast "Yes... The successful predator always starts by separating her chosen prey from the rest of the herd."

                    "...Well now I feel like a fucking creep."

                    beast "You {i}are{/i} a fucking creep. Had you not noticed? I suppose there {i}is{/i} an alternative. Amass enough influence or raw power to gather a herd of your own. Then you can be a different kind of monster."

                    beast "But that would take ambition, work ethic, and a whole bunch of other virtues you don't have. So you'd better get back to hunting, creep."

                    "She watches her friends leave with a hurt expression, then turns to me, wary."

                    cutelady "Hey, uh... can I help you, Miss?"

                    me "Hello, I'm Mindy. Mindy Heng. What's your name?"

                    cutelady "...Ang."

                    me "Pleasure to meet you, Ang. Sorry if this is abrupt, but you look like exactly the sort of person I'd want to interview. What was up with your friends, by the way?"

                    "They're still watching from a distance. She gives them a disgusted look, then turns back to me. While she looks away I take the opportunity to flush my body with Blood, commanding my dead flesh to act like it's alive."

                    "With some effort, Ang raises her voice above the din."

                    ang "Good question. Interview?"

                    $ pc.addPerk(M_LINE_HARDESTADT[KEY_NAME], 1, merit = True)

                    if story_background == "defender":
                        "Fortunately, I don't need to. It's like the ambush, back when I was mortal. My sire shouted and everyone heard every word, no matter how loud everything else got. I must have inherited it from her."
                    else:
                        "Fortunately, I don't. It's a weird thing I can do. I don't think it's the same as the normal Ventrue arts, but I haven't had time to look into it."

                    me "Yeah! I work for Horizon Beat! Sorry, I should have led with that, huh?"

                    ang "I think I've heard of that. Why would you want to interview me?"

                    "And I spin a whole-ass yarn about how I work for the travel blog-slash-zine - which is real - and how I focus on night life. I tell her she looks like the sort of person who knows what to do for fun around here."

                    "With my aura of dread dispelled, she gradually relaxes. After all, normally there's nothing threatening about me. And after a while her eyes start to wander from my face down to other parts of my body. When she thinks I'm not looking."

                    me "So you come here to get away? Like, from...?"

                    ang "Classes, sports, work - you know. The pressures of life."

                    "That'll do. I keep buttering her up, telling her how hip and savvy she seems, while telling grandiose tales about my supposed travels."

            ang "Wow, Mindy. That... sounds like a hell of a lifestyle. Traveling from place to place getting paid to eat, drink and party. And you're doing all that just a few years out of undergrad?"

            "Seven years after dropping out, but who's counting?"

            me "That, and a few other things. I write about {i}every{/i} aspect of a city's night life. It can be a lot of fun, with the right people."

            "I lean forward, and I catch her eyes on my chest for a second before she snaps them back up."

            me "So what did you say you do to blow off steam, again?"

            ang "Uh, well... lots of things."

            "Her friends snicker. They've gotten closer and are listening in, of course. A server is walking by. Ang is practically salivating. Yeah, I've still got it."

            beast "You did well, [pcname]. But preen {i}after{/i} we eat."

            me "Oh yeah? Maybe you could show me? How you have fun? As part of an... interview."

            ang "Yeah, I think I could do that... for an interview. Check, please!"

            scene bg hunt siren_their_place
            play music audio.siren_their_place fadeout 1.5 fadein 1.5 volume 0.8

            "Her place is a cozy studio apartment on the third floor of the Huron-Farouk building on 8th and Cairn. There are books and papers scattered around a laptop, which we head right past on our way to the bed."

            "Given what Ang told me about her life, I probably should have expected her to be pretty good at multi-tasking. She's kissing me hungrily, one of her hands is undoing her belt, and the other is simultaneously grabbing my ass and holding me close."

            "I kiss her back and set to pulling off her shirt. In a few seconds we're on the bed. This would be amazing if I were still alive, but I'm not. So it's just a means to an end. I kiss my way down her chest and stomach."

            "I keep going down, and soon she's sighing and moaning and running her hands through my hair. She doesn't last long. The moment she finishes I bite into her thigh. She cries out in ecstasy again, and I drink it all in."

            $ pc.soundFeed()

            "I can taste the cycle of stress, exertion, triumph, and relaxation that she lives. Sour, spicy, savory, sweet. She works hard and plays hard, leading a life that's arduous, but also full and vibrant. It floods into me, overwhelming me."

            play music audio.freakout fadeout 0.3 fadein 1.5

            beast "I always had faith in you. Now, let's welcome her in. {i}All{/i} of her. She can become one with us, wouldn't that be grand? Then you wouldn't have to be alone."

            "We both know that's not how it works, you lying sack of soul-shit."

            beast "Just because it didn't work last time doesn't mean-"

            "Shut up. Just SHUT UP! I've tasted her magnificence. It's real, unlike the counterfeit impression I use our Blood to give off. She's got an amazing life ahead of her, and I won't steal it away. I force myself to stop."

            $ pc.slakeHunger(2)

            beast "Oh, come on! You don't know that. You're just high on her fumes. She could walk outside the next morning and get run over by a bus for all you know!"

            "She {i}won't{/i}. She's brilliant, she's strong, and she's kind. And... and if she does, it'll be because of this fucked-up, hateful world we crawl around in! Not me. I won't have her death on my hands. {i}Not hers!{/i}"

            beast "What the fuck are you even talking about? You don't even know this girl! Are we a fucking Toreador, to be falling in love with our food? You're Ventrue; act like it! This kind of base sentimentality is beneath us."

            "...Maybe you're right. But we're still not going to kill her, so fuck off with that noise. I kiss her thigh, and the bite wounds close. Her breath is steady, and there's a smile on her face. I start pulling on my clothes."

            "I turn back to look at her. She's rolled onto her side and is snoring softly. I walk over and kiss her forehead. Tears threaten to well up, but I fight them back. Can't start dripping Blood around."

            stop music fadeout 2.0

            beast "What in God's name has gotten into you, [petname]? Was there something in that woman's blood? Or is this just another one of your tantrums?"

            me "I don't know!"

            "Shit, did I say that out loud? I'd better go."

            beast "...Yeah. Let's get the hell out of here."

            $ pc.loseCash(20.0)

            scene black with fade

            return


    # ===CONSENSUALIST HUNTS===
    label .huntX_consensualist:

        scene bg huntX consensualist
        play music audio.consensualist fadeout 0.5 fadein 1.0

        $ picked1 = False
        $ picked2 = False

        "I head down to the strip, to one of the places on [ghoulname]'s list of BDSM clubs and meeting spots. I could try to find someone willing to indulge my \"kink\"."

        beast "...Yeah, I'm gonna sit this one out. You can enjoy interviewing some weirdo in a gimp suit about his deepest fears, or his greatest shame, or... whatever."

        "Fine by me. If you're gonna be like that, just stay asleep while I do all the work as usual."

        beast "Hah! Deal."

        "Or I could just look up one of the escorts in the area. That'd be simpler, but it would cost more."

        label .hx_con_menu:

        play music audio.consensualist fadeout 0.5 fadein 1.0

        menu:
            beast "Just go with your strengths. Such as they are."

            "I inquire after a sex worker who's willing to engage in \"blood play\". It'll be expensive, but it's a safe(r) bet. ([_man] + [_pers])" if not picked1:
                $ picked1 = True
                if story_con_generic1:
                    jump feeding.hx_con_generic
                else:
                    $ grade = evalt(pc.test(hunting_difficulty, _man, _pers, messyCritsOn = True))
                    jump feeding.hx_con_opt1

            "It'll be harder, but I present myself as an experienced participant in kink and see if I can get some \"blood play\" started on my own. ([_man] + [_perf])" if not picked2:
                $ picked2 = True

                if story_con_generic2:
                    jump feeding.hx_con_generic
                else:
                    $ grade = evalt(pc.test(hunting_difficulty + 1, _man, _perf, messyCritsOn = True))
                    jump feeding.hx_con_opt2

            "Forget it. This was a mistake. Looks like we're going hungry for now.":
                beast "Are you FUCKING kidding me?!"

        # NOTE: CONSENSUALIST FAILURE STATE, reached by passing through the menu without jumping.
        play music audio.huntfailure fadeout 0.3 fadein 1.0

        beast "I know you're used to screwing things up, but this is impressive even for you."

        "Stop."

        beast "You know what happens next is going to be your fault, right?"

        "Please. I'm sorry."

        beast "And you know that I don't ask. I {i}take.{/i} Until I'm satisfied. Keep that in mind the next time you feel like pretending to be virtuous."

        "..."

        return


        # CONSENSUALIST OPTION 1
        label .hx_con_opt1:

            $ story_con_generic1 = True

            if grade == MESSYCRIT: # messy crit
                $ pc.soundFeed()

                "..."

                "Shit. I'm taking too much."

                beast "No such thing, baby."

                "Fuck! I focus my willpower and force myself to stop! I lick away the puncture wounds on her forearm."

                python:
                    pc.damage(KEY_WP, KEY_SPFD, pc.getWillPenalty())
                    pc.slakeHunger(3)
                    if pc.getHumanity() > 6:
                        pc.loseCash(200.50)

                beast "Oh come on! And why are you paying? She's unconscious."

                "Shut up. I grab her phone. There's a passcode, but I can use the emergency call function without logging in. I dial 911 and leave it on."

                beast "Sigh... We need to go."

                "I go."

                $ pc.soundFlee()

            elif grade == SUCCESS: # success
                escort "...Okay, since you seem really nice. And I don't get to work with women often. But that's definitely going to cost extra."

                me "Sure."

                escort "So how exactly does this-"

                "I bite into her wrist."

                $ pc.soundFeed()

                "I take no more than what I need, and no more than she can spare. Then I tell her to forget about all this."

                python:
                    pc.slakeHunger(2)
                    pc.cloudMemory()
                    pc.loseCash(200.50)

                beast "You're no fun. Wait, why are you paying after wiping her memory?"

            elif grade == FAIL: # failure
                escort "Uh... no. I don't think so. That doesn't sound safe for either of us."

                beast "You gotta be fucking kidding me."

                me "I can assure you it's perfectly-"

                escort "I'd like you to leave."

                me "Leaving. Sorry."

                beast "No! Just fucking eat her. We came all this way!"

                "Well that could have gone better."

                beast "For fuck's sake!"

            else: # bestial failure
                play music audio.freakout fadeout 0.3 fadein 1.0

                escort "Get away from me!"

                beast "Fuck this FUCK THIS fUcK tHiS fuckthisfuckthisfuckthisfuckthisfuckthis"

                "Stop it. Calm down. Is that a hole in the wall? Stop it! Fuck!"

                escort "Hello, 911?"

                "I focus my will, and force my Beast back down. Then I grab the poor woman's face and stare into her eyes."

                $ pc.damage(KEY_WP, KEY_SPFD, pc.getWillPenalty())

                beast "You useless piece of shit! Why can't you do anything right? Why can't you-"

                me "I'm so sorry. Just forget about this, okay?"

                $ pc.cloudMemory()
                $ pc.soundFlee()

                "She blinks, suddenly confused and unsure. I grab her phone, press the button to hang up, toss it on the bed and I run for it."


        if grade == MESSYCRIT or grade == SUCCESS:
            jump feeding.hx_con_win
        else:
            jump feeding.hx_con_menu


        # CONSENSUALIST OPTION 2
        label .hx_con_opt2:

            $ story_con_generic2 = True

            if grade == MESSYCRIT:
                kinkster "That sounds amazing, actually. So d you want me to start?"

                me "...Sure."

                play sound audio.bite1

                "I may have gotten in over my head with this one. But I want what I came for and this is how I got him to agree, so for the next several minutes I let him run his various blades and knives over my bare arms and legs."

                beast "\"Knife play\", huh? Interesting."

                $ pc.damage(KEY_HP, KEY_SPFD, 2)

                "I'm not sure what this guy's getting out of this, but he's clearly enjoying himself. To his credit, he stops periodically and asks if I want him to continue. What I want is his blood, but I smile and tell him that I like what he's doing."

                if pc.hasDisciplinePower(_fortitude, FORT_HP) or pc.hasDisciplinePower(_fortitude, FORT_TOUGH):
                    "I mean, I can't exactly complain if he asks for my blood in return for his own, can I? And I have to admit that I am a bit fascinated by how my body is handling the careful cuts he's making. I almost have to force my flesh to yield to the blades."
                else:
                    "I mean, I can't exactly complain if he asks for my blood in return for his own, can I? Even if he's a mortal and doesn't have a Kiss to replace the pain with pleasure."

                "I've used the Blush, but I still have to remember to will my Blood to ooze out of the wounds in rivulets, as if it were the blood of a living human being and not the syrupy ichor of an animated corpse."

                kinkster "...May I?"

                me "Go ahead."

                "Might as well. There's no way I'm not wiping this guy's memory. I let him have a taste, and I can tell that he has to force himself to stop lapping up more than I gave him permission to do."

                "But eventually, it's my turn. He nods and opens his red buttoned-down shirt."

                kinkster "You handled that amazingly well. You must have quite a bit of experience. You've got to tell me what you do to hide the scars; your skin looks flawless."

                $ pc.soundFeed("You have no idea.")

                $ pc.slakeHunger(3)

                "He gasps and sighs. I take more than I usually do, but I'm pretty sure he'll be fine. He has a lot of experience with this sort of thing. When I'm done feeding I'm almost sad to wipe his memory. I feel like I've found a kindred spirit, so to speak."

                beast "..."

            elif grade == SUCCESS:
                kinkster "This isn't how it's usually done, but I'm interested. And I don't meet many people with your level of enthusiasm for consensual bloodletting. Go ahead."

                me "I think you'll like it this way."

                $ pc.soundFeed()

                "And I drink. Just what I need."

                beast "..."

                $ pc.slakeHunger(2)

                kinkster "...Wow. That was... incredible. How did you even do that?"

                me "Don't worry, handsome. Just forget about it."

                $ pc.cloudMemory()

                "And I'm gone. Hopefully he remembers the fun part without retaining the who or how."

            elif grade == FAIL:
                kinkster "...What do you think you're doing? You can't just... {i}bite{/i}! Not like that. You don't know what you're doing at all, do you?"

                beast "..."

                me "Of course I do, I was just-"

                kinkster "Yeah, I don't think I'm comfortable doing this with you anymore."

                me "But-"

                "He gives me a distasteful look, then gets up with his gear."

                me "Shit. Okay, just forget about it."

                "He blinks, then turns and walks back out into the main room."

                $ pc.cloudMemory()

                beast "..."

            else: # default is bestial failure, which should be rare
                play music audio.freakout fadeout 0.3 fadein 1.0

                kinkster "Jesus Christ, what are you doing?! Stop!"

                beast "Drink him! Fucking drink him! Before he calls-"

                "Goddamnit! Shut up! SHUT. UP."

                $ pc.damage(KEY_WP, KEY_SPFD, pc.getWillPenalty())

                me "Forget!"

                "His face slackens in confusion, and I surreptitiously make my way out. It's pretty loud in the main room and I'm really hoping no one heard the crash or his screams."
                $ pc.soundFlee()

        if grade == MESSYCRIT or grade == SUCCESS:
            jump feeding.hx_con_win
        else:
            jump feeding.hx_con_menu


        label .hx_con_win: # NOTE: CONSENSUALIST SUCCESS STATE

            play music audio.huntsuccess_cons fadeout 1.0 fadein 1.0 volume 0.6

            beast "As always, I remain skeptical of your virtue signalling pageantry. But you got results, and in the end that's what matters. Well done."

            "What's wrong with virtue signalling, as long as it's consistent? Actions have consequences, regardless of the intent behind them. We are what we pretend to be."

            beast "You think that pretending you're not a monster will somehow make you cease to be one?"

            "What's the material difference? Why should I waste energy constantly interrogating my own state of mind? The right thing to do is the same either way."

            beast "So, refuge in delusion and hypocrisy? That's your answer?"

            "If it helps, sure. If I consistently do the best I can, who cares if I'm secretly a hypocrite deep down? A tree is judged by the fruit it bears."

            beast "But the fruit always goes rotten eventually. You'll lose it again. It's inevitable."

            "That's no reason not to do my best in the meantime."

            beast "..."

            $ pc.mend(KEY_WP, KEY_SPFD, 1)
            stop music fadeout 2.0
            scene black with fade
            $ updateTime(0.5)
            return

        label .hx_con_generic:

            $ grade = evalt(pc.test(hunting_difficulty, _man, _pers))

            if grade == SUCCESS or grade == MESSYCRIT:
                "I spend the night hitting my usual spots. After a while I refine my techniques to the point where I don't always have to wipe their memories."

                "It feels good to get what I need this way. No coercion beyond baseline capitalism, and only a minimal amount of lying. The kind I have to do for my job anyway."

                beast "As long as you get results..."

                $ pc.slakeHunger(2)
                $ pc.loseCash(150)
            else:
                "There's an art to getting a human being to willingly let you drink their blood. Tonight I seem to be in a creative slump."

                "None of the usual contacts I've developed among the sex work and kink communities are available."

                "I try to engage promising candidates in conversation, but I can't really get anywhere."

                beast "...Don't lose focus now. Things will go badly if you do."

            $ updateTime(0.5)
            return


    # ===ROADSIDE KILLER HUNTS===
    label .huntX_roadsidekiller:

        scene bg huntX roadsidekiller

        play music audio.roadside_killer fadeout 0.5 fadein 1.0

        $ picked1 = picked2 = used_dominate = used_presence = False

        "I head into the city, to one of the spots on [ghoulname]'s list of places with heavy traffic. Should be lots of folks on the move around there."

        beast "We need to get someone talking to us, or look for other obvious signs of flight."

        "The way I see it, we can drive around parking lots and look for a pedestrian that seems like our type, or we can try to follow someone on the road."

        label .hx_rsk_menu:

        play music audio.roadside_killer fadeout 0.5 fadein 1.0

        menu:
            beast "Our mental powers can help here. Just don't fucking crash."

            "I haunt parking lots, driving slow and casual, looking for any suitable stragglers I can draw. ([_cha] + [_driv])" if not picked1:
                $ picked1 = True
                if story_rsk_generic1:
                    jump feeding.hx_rsk_generic
                else:
                    $ grade = evalt(pc.test(hunting_difficulty, _cha, _driv, messyCritsOn = True))
                    jump feeding.hx_rsk_opt1

            "I look for suitable stragglers. When I find one, I pull up and command them to get in. This is the surest bet, but I'm risking more Hunger. ([_man] + [_dominate])" if not picked1 and pc.hasDisciplinePower(_dominate, DOM_MESMERIZE):
                $ picked1 = used_dominate = True
                if story_rsk_generic1:
                    jump feeding.hx_rsk_generic
                else:
                    $ pc.addHungerDebt(4)
                    $ grade = evalt(pc.test(hunting_difficulty - 1, _man, _dominate, messyCritsOn = True))
                    jump feeding.hx_rsk_opt1

            "This will be tricky, but I take to the highway and try to follow a suitable looking vehicle to their destination. ([_dex] + [_driv])" if not picked2:
                $ picked2 = True
                if story_rsk_generic2:
                    jump feeding.hx_rsk_generic
                else:
                    $ grade = evalt(pc.test(hunting_difficulty + 1, _dex, _driv, messyCritsOn = True))
                    jump feeding.hx_rsk_opt2

            "I take to the highway and try to follow a suitable looking vehicle to their destination. This will be tricky, but my supernatural charisma will smooth things over if my natural charisma doesn't. ([_cha] + [_driv] + [_presence])" if not picked2 and (pc.hasDisciplinePower(_presence, PRES_AWE) or pc.hasDisciplinePower(_presence, PRES_CHARM)):
                $ picked2, used_presence = True
                if story_rsk_generic2:
                    jump feeding.hx_rsk_generic
                else:
                    if pc.hasDisciplinePower(_presence, PRES_AWE):
                        $ pc.awe()
                    else:
                        $ pc.entrance()
                    $ grade = evalt(pc.test(hunting_difficulty + 2, _cha, _driv, _presence, messyCritsOn = False, bestialFailsOn = False))
                    jump feeding.hx_rsk_opt2

            "Forget it. This was a mistake. Looks like we're going hungry for now.":
                beast "Are you FUCKING kidding me?!"

        # NOTE: ROADSIDE KILLER FAILURE STATE, reached by passing through the menu without jumping.
        play music audio.huntfailure fadeout 0.3 fadein 1.0

        beast "How? HOW?! How do you fuck this up?"

        "..."

        beast "You know what happens next is going to be your fault, right?"

        "Shut up. Just shut up."

        beast "Oh I will, you utter idiot. When I take over and I've gorged myself you can trust I'll be quiet for at least a night or two."

        "..."

        return


        # ROADSIDE KILLER OPTION 1
        label .hx_rsk_opt1:

            $ story_rsk_generic = True

            if grade == MESSYCRIT: # messy crit
                $ pc.soundFeed()

                "...Uh oh. He's lost a lot of blood."

                beast "So? Who's gonna miss {i}this{/i} guy?"

                "I don't know. That's not the point. I force myself to stop."

                $ pc.damage(KEY_WP, KEY_SPFD, pc.getWillPenalty())
                $ pc.slakeHunger(3)

                if not used_dominate:
                    "I grab his smartphone. There's a passcode, but I can use the emergency call function without logging in. I dial 911 and leave it on."
                else:
                    "Hope this poor guy doesn't get fucking brain cancer or anything. I dial 911 on his phone and dip."

                beast "Sigh... We need to go."

                "Yeah."
                $ pc.soundFlee()

            elif grade == SUCCESS: # success
                someguy "So then I get the call. They went with someone else. And at that point, there just wasn't anything left for me in Missouri, you know?"

                if not used_dominate:
                    me "Sometimes you need a fresh start. You'll do better in Arizona, I'm sure."

                    someguy "Well I appreciate the vote of confidence, Ms... what did you say your na-"
                else:
                    me "Sure. Step over here behind that dumpster with me, please. Walk casually and stay quiet."

                    someguy "..."

                $ pc.soundFeed()

                "...There. That'll have to be enough."

                someguy "...Huh? What?"

                $ pc.slakeHunger(2)

                "I've already disappeared into the shadows. I double back around and head back to my car across the lot. Don't even need to wipe him."

                beast "..."

            elif grade == FAIL: # failure
                if used_dominate:
                    someguy "Uh, what? I'm not going anywhere with you, lady."
                else:
                    someguy "Listen, ma'am. I appreciate the concern, but I'm not gonna discuss my personal life with some strang-"

                me "I just wanted to-"

                "He's already backing off, headed back towards the well-lit part of the lot. Too many people around to chase him. Fuck."

                beast "Great job. Fantastic."

            else: # bestial failure
                play music audio.freakout fadeout 0.3 fadein 1.0

                someguy "Oh my God. Oh my God! You're fucking crazy! Get off me! Someone help!"

                play sound audio.beastgrowl1

                beast "I'll show you crazy, you ugly, balding fuck!"

                play sound audio.punchgrunt1

                someguy "Ahh! HELP!"

                "Stop it. STOP IT!"

                "I force my Beast down, then grab this poor guy's head and force him to look at me."

                me "Forget!"

                $ pc.damage(KEY_WP, KEY_SPFD, pc.getWillPenalty())
                $ pc.cloudMemory()

                "I make a run for it. At least I made sure there weren't any cameras."
                $ pc.soundFlee()

            if grade == MESSYCRIT or grade == SUCCESS:
                jump feeding.hx_rsk_win
            else:
                jump feeding.hx_rsk_menu


        # ROADSIDE KILLER OPTION 2
        label .hx_rsk_opt2:

            $ story_rsk_generic = True

            if grade == MESSYCRIT:
                play sound audio.car_screech volume 0.6

                "Oh no. Oh no no no."

                me "Fuck!"

                "I ran her off the road. I ran her off the fucking road. I pull over onto the shoulder. Please, God, let her be okay."

                beast "She looks more than okay. She looks delicious."

                carlady "{alt}Moaning: {/alt}Ughhh..."

                "For fuck's sake, not now! ...Okay. She's breathing, she's conscious. She's dazed. She's fine. I think. I need to call 91-"

                $ pc.soundFeed()

                beast "Oh yeah."

                "No! What the fuck? ...How did I even get into her car? Stop!"

                python:
                    pc.damage(KEY_WP, KEY_SPFD, pc.getWillPenalty())
                    pc.slakeHunger(2)

                "Oh God. What the fuck have you done?"

                beast "Sustained us for another night. Would have been longer if you hadn't interrupted."

                "Okay, she's still breathing. It's fine. And I stopped you before you took too much. It's fine. I lick the wound."

                $ pc.soundFlee()

            elif grade == SUCCESS:
                if used_presence:
                    carlady "I just... the hubbie, the kids. I needed to get away from it all. Just for a week or so. You understand, right? I feel like I could tell you anything."
                else:
                    carlady "I just... the hubbie, the kids. I needed to get away from it all. Just for a week or so. You get it, right?"

                me "I sure do, honey. I sure do."

                $ pc.soundFeed()

                "And I drink. Only what I need."

                beast "..."

                $ pc.slakeHunger(2)

                "And I'm gone. She should be fine asleep in her car. This parking lot's pretty high-traffic."

            elif grade == FAIL:
                carlady "Uh... hi?"

                me "Hey, I was wondering if you had a few minutes to talk abou-"

                carlady "Oh my God, fuck off."

                beast "...Really? {i}That{/i} was your line?"

                me "Shut up."

            else: # default is bestial failure, which should be rare
                play music audio.freakout fadeout 0.3 fadein 1.0

                carlady "What are you doing? Get away! Help!"

                play sound audio.beastgrowl1

                beast "..."

                "Fuck fuck fuck stop!"

                $ pc.damage(KEY_WP, KEY_SPFD, pc.getWillPenalty())

                me "Forget! Sorry!"

                beast "You incompetent fucking-"

                "I run for it."

                $ pc.soundFlee()

        if grade == MESSYCRIT or grade == SUCCESS:
            jump feeding.hx_rsk_win
        else:
            jump feeding.hx_rsk_menu


        label .hx_rsk_win: # NOTE: ROADSIDE KILLER SUCCESS STATE

            play music audio.huntsuccess fadeout 1.0 fadein 1.0 volume 0.6

            beast "Another successful hunt. You might just get good at this one day."

            "..."

            beast "And then, we can really start living once you get over these weird hangups you have about \"human life\". Please, you saw those people. Did they seem like the type the world just can't do without?"

            "I'm not listening to any of your shit for at least another night."

            stop music fadeout 2.0
            scene black with fade
            $ updateTime(0.5)
            return

        label .hx_rsk_generic:
            $ grade1 = evalt(basictest(hunting_difficulty, _cha, _driv, _dominate))
            $ grade2 = evalt(basictest(hunting_difficulty, _dex, _driv, _presence))

            if grade1 == SUCCESS or grade2 == SUCCESS:
                "The thing about feeding from transient populations is that it takes quite a bit longer for rumors to get around. It also helps that I'm careful not to kill anyone unless they come at me first. Even then I'm usually a good sport about it."

                "The hard part is getting people to talk to me, but I manage."

                $ pc.slakeHunger(2)
            else:
                "Sometimes failure means success at an untenable cost."

                "Venturing into some of the rougher areas is a great way to find prey that suits my needs. It's also a great way to get jumped."

                "Still, getting stabbed and shot isn't quite the emergency for Kindred that it is for mortals. Better than letting my Beast swallow me whole."

                beast "That's the spirit. And maybe next time you can hunt like you have two brain cells to rub together."

                $ pc.slakeHunger(2)
                $ pc.damage(KEY_HP, KEY_SPFD, 4)

            $ updateTime(0.5)
            return


    # ===SCENE QUEEN HUNTS===
    label .huntX_scenequeen:

        scene bg huntX scenequeen

        play music audio.scene_queen_x fadeout 0.5 fadein 1.0

        $ picked1 = picked2 = used_contacts = used_presence = False

        "I head into the city, to one of the clubs on [ghoulname]'s list. Hopefully we can treat ourselves to some dancing and dinner."

        label .hx_sqn_menu:

        play music audio.scene_queen_x fadeout 0.5 fadein 1.0

        menu:
            beast "This is supposed to be your element, so do your thing."

            "I've introduced myself to the owner and staff here. I'll spread some money and love around, get people watching, then conquer the dance floor. ([_cha] + [_perf])" if not picked1:
                $ picked1 = True
                if story_sqn_generic1:
                    jump feeding.hx_sqn_generic
                else:
                    $ grade = evalt(pc.test(hunting_difficulty, _cha, _perf, messyCritsOn = True))
                    jump feeding.hx_sqn_opt1

            "I've introduced myself to the owner and staff here. I'll spread some money and love around, get people watching, then conquer the dance floor with my supernatural Ventrue allure. ([_cha] + [_perf] + [_presence])" if not picked1 and (pc.hasDisciplinePower(_presence, PRES_AWE) or pc.hasDisciplinePower(_presence, PRES_CHARM)):
                $ picked1 = used_presence = True
                if story_sqn_generic1:
                    jump feeding.hx_sqn_generic
                else:
                    if pc.hasDisciplinePower(_presence, PRES_AWE):
                        $ pc.awe()
                    else:
                        $ pc.entrance()
                    $ grade = evalt(pc.test(hunting_difficulty + 1, _cha, _perf, _presence, messyCritsOn = False, bestialFailsOn = False))
                    jump feeding.hx_sqn_opt1

            "My contacts should be helpful here. I talk to the owner and have him have the staff send someone my way. On a totally unrelated note, I furnish the owner of with a small consideration, as a token of respect. ([_man] + [_intr] + Contacts)" if not picked2 and pc.hasPerk(M_CONTACTS[KEY_NAME])[0]:
                $ picked2, used_contacts = True
                if story_sqn_generic2:
                    jump feeding.hx_sqn_generic
                else:
                    $ contactsLevel = pc.hasPerk(M_CONTACTS[KEY_NAME])[0]
                    $ grade = evalt(pc.test(hunting_difficulty, _man, _intr, M_CONTACTS[KEY_NAME], messyCritsOn = False, bestialFailsOn = False))
                    jump feeding.hx_sqn_opt2

            "Forget it. This was a mistake. Looks like we're going hungry for now.":
                beast "Are you FUCKING kidding me?!"

        # NOTE: SCENE QUEEN FAILURE STATE, reached by passing through the menu without jumping.
        play music audio.huntfailure fadeout 0.3 fadein 1.0

        beast "THIS WAS SUPPOSED TO BE YOUR ELEMENT!"

        "I... I just..."

        beast "You know what happens next is going to be your fault, right?"

        "No. No, we're not doing th-"

        beast "Then, dear [pcname], you better figure something out REAL FUCKING QUICK!"

        "...Alright, alright."

        return


        # SCENE QUEEN OPTION 1
        label .hx_sqn_opt1:

            if grade == MESSYCRIT: # messy crit
                $ pc.soundFeed()

                "...What happened? I'm backstage. There was a blur of dancing and cheering, a beautiful young woman, then... oh. Oh shit. Stop!"

                beast "OH COME ON"

                "We're letting go of her NOW."

                $ pc.damage(KEY_WP, KEY_SPFD, pc.getWillPenalty())
                $ pc.slakeHunger(3)

                "I lick the wound and let one of the staff know about my unfortunate friend. I tell them she passed out and might have alcohol poisoning. They'll get her some help."

                beast "Sigh... If you're cutting the fun short we should just go."

                "Yeah. Shit, was she on something? Why's everything so...? Uh oh. Oh, fuck. I don't think I can drive like this. I'm gonna have to call a Lyft or something..."

                $ pc.loseCash(150.15)

                beast "Unbelievable."

                $ pc.soundFlee()

            elif grade == SUCCESS: # success
                me "So you flew all the way out here from West Gloucestershire?"

                edmlady "Yeah. Studying abroad. Technically. Really, I just needed to get out of England for a while. It's not a very welcoming place if- ...well, let's not get into politics."

                edmlady "But that was exhilarating back there! On the floor? You're crazy good. The whole crowd was loving you. The way you worked that as- uh, I mean... Sorry, that was rude."

                me "{alt}Laughing: {/alt}No worries. From you, I take it as a compliment."

                edmlady "I definitely meant it as one. Wait, are you like, famous?"

                me "Me? Nah. Some people in the scene know me and I do a little choreography."

                edmlady "I knew it! This is so freaking cool. Thanks for inviting me backstage. Did you want to... I mean, I'm holding. ...If you're into that sort of thing."

                me "Sure, sounds great."

                $ pc.soundFeed("As she reaches into her purse, I bite into her bare shoulder. I'd love to partake of her after she partakes, but I've got a job to do.")

                beast "Showing up to work high would be bad even for you."

                if used_presence:
                    edmlady "Oh! Mmm, if you wanted that, all you had- oh..."

                    "I don't blame you, honey. I can't get enough of me either."

                    beast "..."
                else:
                    edmlady "What are you... doing? That feels..."

                    "Don't worry about it. It'll be over soon."

                "...There. That'll have to be enough."

                edmlady "...Mmm"

                me "Thanks for the fix, babe. Just forget about all this, okay?"

                $ pc.slakeHunger(2)
                $ pc.cloudMemory()

                "I've already disappeared."

            elif grade == FAIL: # failure
                if used_presence:
                    edmlady "Umm, you're really sweet, but... I don't think so."
                else:
                    edmlady "Uh, no? I'm not going anywhere with you. Creepy-arse..."

                "She's already walking hurriedly away. Fuck. I must be real fucking rusty."

                beast "Once again, you've managed to snatch defeat from the jaws of victory. Are you noticing a pattern? Because I sure am."

                "Stuff it."

            else: # bestial failure
                play music audio.freakout fadeout 0.3 fadein 1.0

                "Onlooker 1" "What is she doing? Is she having a bad trip or what?"

                "Onlooker 2" "Hey! Get off of her."

                "Onlooker 3" "Someone call security!"

                play sound audio.beastgrowl1

                beast "Fuckyoufuckyoufuckyoufuckyoufuckyou"

                edmlady "Get the fuck off me!"

                "Oh God."

                $ pc.damage(KEY_WP, KEY_SPFD, pc.getWillPenalty())

                me "Forget!"

                python:
                    if not pc.hasPerk(M_LINE_HARDESTADT[KEY_NAME])[0]:
                        pc.addPerk(M_LINE_HARDESTADT[KEY_NAME], 1, merit = True)

                "My voice trick is all that saves me. I get the screaming woman and the two onlookers that saw the most."

                python:
                    pc.cloudMemory()
                    pc.cloudMemory()
                    pc.cloudMemory()
                    pc.loseCash(500)

                "It's gonna take a lot of mea culpas of the green variety to smooth this over. Assuming I don't want to be banned from half the clubs in the city."

                $ pc.soundFlee()

                "Just fucking great."

            if grade == MESSYCRIT or grade == SUCCESS:
                jump feeding.hx_sqn_win
            else:
                jump feeding.hx_sqn_menu


        # SCENE QUEEN OPTION 2
        label .hx_sqn_opt2:

            if grade == MESSYCRIT or grade == SUCCESS:
                $ pc.loseCash(150)

                hollowman "Hey. So I was told to come see you, for..."

                "He's tall and lean, with striated muscles and a six pack visible beneath his Under Armour. Strong jaw, ash-blonde hair. Grey sweatpants. Handsome, or at least he used to be. He looks like he hasn't slept in three days. He's nervous and twitchy, but I can't tell if it's drugs, sleep-deprivation or fear."

                me "Yeah. You okay?"

                hollowman "Eh, better than usual. You're a lot better-looking than most of the people they send me to, uh..."

                "I don't know what this guy thinks he's here to do, and I'm not sure I want to find out. I don't even need to talk to him to know he's my type."

                me "Sit down. Relax. It's not gonna be that bad."

                hollowman "...Sure."

                "I take his hand, and hold up his arm to my mouth."

                hollowman "Aw man, you're not a biter, are you? I just-"

                $ pc.soundFeed()

                hollowman "Ouch! Oh. Oh shit..."

                beast "This guy's a fucking wastoid. He doesn't even look like he {i}wants{/i} to be alive. Let's welcome him in. Take away his suffering for good."

                "Shut up."

                $ pc.slakeHunger(2)

                hollowman "...Wow. I, what did-"

                me "Forget about it, handsome. You'll be okay."

                $ pc.cloudMemory()

                beast "You're such a fucking liar."

            else:
                "Club Owner" "Sorry, [petname]. We don't have anyone available. We'll comp you with free drinks."

                me "...Sure. Thanks anyway, man. Give \"Jack\" my regards."

                beast "Great work, genius. So much for your \"connections\"."

                "..."

        if grade == MESSYCRIT or grade == SUCCESS:
            jump feeding.hx_sqn_win
        else:
            jump feeding.hx_sqn_menu

        label .hx_sqn_win: # NOTE: SCENE QUEEN SUCCESS STATE

            play music audio.huntsuccess fadeout 1.0 fadein 1.0 volume 0.6

            beast "Nightclubs are just the best, aren't they? Like an all-you-can-eat buffet."

            "Pretty much."

            beast "Don't get cocky, though."

            "Who, me?"

            "But this {i}was{/i} a pretty good night. All things considered."

            stop music fadeout 2.0
            scene black with fade

            $ updateTime(0.5)
            return

        label .hx_sqn_generic:

            "This is my element, and most owners and staff throughout the scene are happy to see me. I'd be having a ball if not for the Hunger chewing at the back of my brain."

            "Fortunately, finding prey is easy here. And easy means far less chance of accidents."

            $ pc.slakeHunger(2)
            $ updateTime(0.5)


    # ===SIREN HUNTS===
    label .huntX_siren:

        scene bg city nightscape1

        play music audio.siren_women1 fadeout 0.5 fadein 1.0

        python:
            picked1 = picked2 = used_presence = False
            exname = pcex["first"]
            exlast = pcex["last"]
            exsubj = pcex["subj"]
            exSubj = str(exsubj).capitalize()
            exobj = pcex["obj"]
            expos = pcex["pos"]

            if story_orientation == SIREN_BOTH:
                story_this_time = SIREN_WOMEN if random.randint(0, 1) > 0 else SIREN_MEN
            else:
                story_this_time = story_orientation

        "I head into the city, to one of the clubs on [ghoulname]'s list. Hopefully we can find a little romance and fine dining."

        beast "Alright, sexpot. Do your thing. Wake me up when it's time for dinner."

        if story_srn_generic:
            jump feeding.hx_srn_generic

        "Sure, just watch me-"

        "...Oh shit. No, no, no..."

        beast "What? What is it?"

        "Standing about a block away, waiting to cross the street, is my ex. [exname] [exlast]."

        beast "Another fucking distraction. Do whatever you need to do. I recommend eating [exobj] and tossing what's left down a manhole."

        menu:
            "Jesus Christ. No, we're not doing anything like that. Just shut up and let me think."

            "[exSubj] hasn't seen me yet. If I'm careful and alert I can just sneak around [exobj]. ([_dex] + [_clan] or [_wit] + [_stre])":
                $ grade1 = evalt(pc.test(3 + int(story_times_dodged_ex), _dex, _clan))
                $ grade2 = evalt(pc.test(3 + int(story_times_dodged_ex), _wit, _stre))
                if grade == SUCCESS or grade == MESSYCRIT:
                    "I know [exname] well enough to know how [exsubj] thinks. Keeping her position in mind, I can keep out of [expos] field of view until I'm a safe distance away."

                    beast "When it comes to running from problems like a spineless coward, you truly are peerless. You know [exsubj]'ll just keep looking for you, right?"

                    "Shut up. Let's get back to business."

                    $ story_times_dodged_ex += 1
                    jump expression "feeding.hx_srn_" + story_this_time
                elif grade == FAIL:
                    "Ducking into alleys and hiding behind buildings, always keeping [expos] position in mind, and finally..."

                    "Shit."

                    beast "Way to go, Sam Fisher."

                    $ story_met_ex = True
                    jump feeding.hx_srn_meet_ex
                else: # bestial failure
                    "...Shit. Goddamn it!"

                    beast "Alright, enough. We're done. I'm ending this."

                    stop music fadeout 0.5
                    scene black with fade

                    jump feeding.hx_srn_attack_ex

            "I can literally just {i}make{/i} [exobj] leave. I command [exname] to leave the city! ([_man] + [_dominate])" if pc.hasDisciplinePower(_dominate, DOM_MESMERIZE):
                $ grade = evalt(pc.test(3 + int(story_times_dodged_ex), _man, _dominate))

                "I march up to [exobj]. [exSubj] sees me from a hundred feet away and starts to wave, then thinks better of it."

                exlover "[petname]! It's good to-"

                me "You will leave this city and you will not return."

                if grade == SUCCESS or grade == MESSYCRIT:
                    exlover "...[petname]? Why wou-"

                    "[exSubj] gives me a strange look, then turns around and walks away."

                    beast "Didn't you listen to our sire? You know that's not going to work for long."

                    "...Just shut up. Please."

                    $ story_times_dodged_ex += 1
                    jump expression "feeding.hx_srn_" + story_this_time
                else:
                    exlover "[Beth], why are you doing this? Why are you acting this way? Just talk to me, please! Please."

                    beast "Pathetic."

                    me "...How? Shit."

                    $ story_met_ex = True
                    jump feeding.hx_srn_meet_ex

            "This has gone on long enough. I'm dealing with [exname] for good. I pull [exobj] into a quiet alley and rewrite [expos] memories. It's drastic and cruel, but it's what best for me, [exobj], and the Masquerade." if pc.hasDisciplinePower(_dominate, DOM_GASLIGHT) and story_times_dodged_ex > 2:
                beast "Well look who's finally grown a spine. Not my ideal solution, but it's certainly decisive. And final. Very Ventrue."

                "I march up to [exobj]. [exSubj] sees me from a hundred feet away and starts to wave, then thinks better of it."

                exlover "[petname]! It's good to-"

                me "Come with me, [exname]."

                exlover "Okay, sure. I really just need to talk to you."

                scene bg danger alley1
                # play music audio.brainwashedex fadeout 1.0 fadein 2.5 TODO: need track for this

                jump feeding.hx_srn_brainwash_ex

            "Fuck it. I have to deal with [exobj] sooner or later. I'll go talk to [exname].":
                beast "Well look who's finally grown a spine. I still think you should eat [exobj]."

                jump feeding.hx_srn_meet_ex


        label .hx_srn_brainwash_ex:

            exlover "[petname]. I-"

            "I put my finger to [expos] lips. And then my Blood percolates behind my eyes, roiling and surging back and forth between my tongue and my lips and my brain. My gaze burns into [expos] mind, and [expos] eyes grow wide."

            $ pc.addHungerDebt(4)

            me "You never saw me here in this city. You never saw [ghoulname]. You didn't come here to look for [pcname] [pclast]. You came to see the sights, and you have. It was great fun. You took time off for yourself. Self-care. It was important, and you feel better."

            me "You never needed [petname] [pclast]. You've been doing just fine without her. Better, actually. You planned to leave this city after your vacation and return to your life fresh and rejuvenated. You're free."

            exlover "But... I love her. I love [petname]."

            me "You've been assured by the people you trust the most - family and friends - that those feelings will pass. That they don't need to control you."

            exlover "..."

            "I don't have any way of knowing how much of it took, or how well the implanted narrative will hold up to any kind of reflection or scrutiny. And I can't stick around to find out. I head the other way."

            stop music fadeout 0.5
            scene black with fade

            beast "Had to be done. Problem solved. Back to business."

            me "...Yeah. Back to business."

            $ story_brainwashed_ex = True
            $ story_ex_resolved = True
            jump expression "feeding.hx_srn_" + story_this_time


        label .hx_srn_meet_ex:

            scene bg danger alleyRed with trans_slowfade
            # play music audio.meeting_ex fadeout 1.0 fadein 2.0 TODO: track for this.

            "We're standing in an alley just off the Teknokhrome Plaza. [exname] looks at me, an expression on [expos] face that I can't read."

            exlover "Thanks for coming to talk to me, [petname]."

            me "What do you want? Why are you doing this? Following me from city to city! Are you fucking insane?"

            exlover "I... [petname]. I had to find you. I can't stop thinking about you."

            me "[exname]... don't do this."

            exlover "Wait, just hear me out! Please. I think I'm {i}supposed{/i} to be with you. In one way or another. [petname], haven't you wondered how I keep finding you?"

            "Yeah, I was going to have to look into that at some point."

            if pc.getSkill(_tech) > 2:
                "I swept everything for bugs and trackers. I don't use a personal smartphone anymore. I don't log in to any personal accounts unless I'm behind a half dozen proxies. My work devices are all end-to-end encrypted and everything."
            else:
                "[exname] isn't a particularly \"technical\" person. I swept everything for bugs and trackers. The devices I use for work are all supposed to be secure."

            me "...How you find me, [exname]?"

            exlover "My dreams! I always see you in my dreams."

            me "You've got to be fucking kidding me."

            exlover "It's true!"

            "[exSubj] goes on to describe, in impressive and disturbing, my itinerary over the last week or so."

            me "So, what? You hired a private investigator? You..."

            exlover "I swear, I see you almost every time I sleep!"

            me "You need therapy, [exname]. Not some monomythical Hero's Journey. There are a hundred thousand better places to find meaning in your life."

            "Can mortals do what [exsubj]'s suggesting? My sire told me that some mortals have gifts or abilities that seem to be supernatural. Or is another Kindred involved here?"

            beast "That would be my guess."

            exlover "...Only ever at night, so I have to sleep during the day. But that's not the point. The point is, there has to be a reason for all this."

            "Shit, I wasn't listening for that last part."

            exlover "I'm supposed to be by your side. Helping you, or protecting you. Something. I've never had dreams like this before; it can't be a coincidence!"

            exlover "[petname], I love you. I already forgave you for all the other... things. I need you."

            me "You really, really don't."

            exlover "I do! I know I'd never meet someone else like you in a hundred years."

            me "That's a good thing. We were {i}terrible{/i} for each other. Especially me for you. Why are you putting yourself through this?"

            exlover "But listen - I wouldn't be here if I didn't think there was something I can do for you. Something I'm supposed to do for you."

            beast "That might be the only way to resolve this."

            "What? ...No. No fucking way. I can't do that to [exobj]. Not after everything else."

            beast "Isn't this really bad for the Masquerade? If you're not willing to eat [exobj] or scramble [expos] brains, what other choice is there? Kindred in your line of work can't have mortal stalkers. You want your bosses finding out about this?"

            "..."

            "No. That would be the worst possible outcome. For [exname] and I both."

            menu:
                "I have to do {i}something{/i}, don't I?"

                "This can't go any farther. It's wrong and it's cruel, but I know my job and I what the alternatives are. I use the power of my Blood to rewrite [exname]'s memories." if pc.hasDisciplinePower(_dominate, DOM_GASLIGHT):
                    jump feeding.hx_srn_brainwash_ex

                "I guess [exname] really is my responsibility after all. I did this to [exobj]. Some of it, at least. There's only way forward that doesn't involve [expos] death. I make [exname] into my second retainer.":
                    beast "..."

                    me "Alright."

                    exlover "But [petname], I- ...what?"

                    me "We can be together, if you think it has to be that way. But there's a price. It'll cost you whatever you have left."

                    exlover "...What? [petname], if you need money I can-"

                    me "Not what I meant. I mean it'll cost you whatever life and happiness you would have had."

                    exlover "...I accept. A small price to pay. This is destiny. I believe that."

                    me "...We'll see. Kneel."

                    exlover "Uhh... okay."

                    "[exname]'s eyes widen as I flip my switchblade open and cut my wrist. No one's around. No one can see us in the shadows here. We're not in any cameras' field of view."

                    exlover "Uh, [petname]? What kind of weird shit are you into these days?"

                    me "You're about to find out, aren't you? Drink."

                    "[exSubj] does as [exsubj]'s told without another word. I don't know why I'm surprised. [exSubj] drinks and drinks, until I tear my arm away from [exobj] and seal the wound. [exname] stares up at me with what looks like wonder. Or horror."

                    exlover "...I knew it, [petname]. I knew this was meant to be. This is proof."

                    me "Here's the address of the hotel I'm staying at. Wait for me there in the lobby."

                    exlover "Anything. God, I love you so much."

                    beast "Yes, this is good. Another loyal servant to do our bidding. [exSubj] certainly asked for it. Probably be happier this way, if anything."

                    "..."

                    $ story_ghouled_ex = True
                    $ story_ex_resolved = True
                    jump expression "feeding.hx_srn_" + story_this_time


        label .hx_srn_attack_ex:

        $ story_attacked_ex = True

        play music audio.freakout fadein 2.0

        scene bg danger alley1

        "..."

        "...What happened? Where am I?"

        beast "Your ineptitude was pissing me off, so I'm solving your problem for you."

        "...What problem? What are you- NO! STOP!"

        beast "It's time someone finally stepped up and dealt with this issue."

        "My hands are wrapped around [exname]'s throat. [exSubj]'s giving me that look. That sad, betrayed, pathetic look that makes me want to kill myself and maybe [exobj] too. [exSubj]'s not even fighting back! Oh God. STOP IT! PLEASE! pleasepleasepleasepleasepleaseplease stopitstopitstopitstopitstopitstopit"

        $ pc.damage(KEY_WP, KEY_SPFD, pc.getWillPenalty())
        $ pc.slakeHunger(2)

        "[exSubj] gasps for air."

        stop music fadeout 2.5

        exlover "{alt}Gasping, choking: {/alt}Wasn't sure how you'd react to seeing me again. I thought I was prepared for the worst, but once again you manage to surprise me."

        me "...[exname]? Why are you here? How did you find me?"

        "[exSubj] gives me a long, sad look."

        exlover "I had to... I needed to-"

        "Onlooker" "What the hell is going on here? Oh my God!"

        "Onlooker" "What the hell is she doing? Someone call the cops!"

        "Onlooker" "Holy shit."

        me "Fuck!"

        exlover "Wait! [petname], I-"

        me "Forget!"
        $ pc.cloudMemory()

        "[exSubj]'s eyes glaze over, and I {i}run{/i}."

        $ pc.soundFlee()

        scene black with fade
        return


        label .hx_srn_men:

        scene bg huntX siren

        if story_srn_generic:
            jump feeding.hx_srn_generic

        $ story_siren_generic = True

        "I make my way onto the dance floor doing some basic dancehall moves. A few heads are turning already. I head to the clear space with the best lighting."

        if pc.hasDisciplinePower(_presence, PRES_DAUNT):
            "Over the next few minutes a few creeps get close, trying to grind on me without an invitation. I flex my aura at them and they slink away, suddenly remembering their manners."
        else:
            "I have to dodge a few creeps trying to grind on me without an invitation. Ugh."

        "I also pass by a few guys that seem nice but just aren't up to par. Not my type (in the normal, aesthetic sense), or just bad dancers. But then I see a promising candidate, leaning against the bar chatting with his boys."

        if pc.hasDisciplinePower(_presence, PRES_AWE):
            "The moment he looks my way I reel him in with my aura. Not that I needed it, judging by the way his gaze slides up and down by body. But I need to move things along. He makes his way over, and he's actually a fairly good dancer."
        else:
            "The moment he looks my way, I have him. His gaze wanders up and down. I give him a wink, and his boys egg him on. He makes his way over, and he's actually a fairly good dancer."

        "He can actually do things other than two-step and grind on my ass. When did men forget how to dance, anyway? Don't they teach these boys anything these days?"

        beast "Focus, \"Salome\"."

        "Fuck off. I enjoy myself for a few minutes, until the song changes and we head back to the bar. A few minutes of conversation and I have what I need. Something about a toxic family that doesn't accept him for who he is. Close enough."

        "I suggest we get out of here. He smiles; it's his lucky night. His place is two-bedroom apartment on 20th and Terminex. We don't make it to the bed."

        $ pc.soundFeed("The sex is pretty good, considering that I'm dead. When he starts nibbling at my ear I turn my head and bite into his lip. He makes a sort of yelp that deepens into a moan halfway through. I drink as much as I dare, then kiss the wounds away.")

        beast "Must our every victory be incomplete and hollow? Why not invite him in? I mean all of him, all the way in. You could use another friend."

        "You tried this once before, asshole. We both know that's not how it works. I pull my clothes back on and slip out the door."

        jump feeding.hx_srn_win


        label .hx_srn_women:

        scene bg huntX siren

        if story_srn_generic:
            jump feeding.hx_srn_generic

        $ story_siren_generic = True

        "I don't care for the music here - it's not bad per se, but it doesn't make we want to dance at all. So I sit down at the bar and order a drink I won't touch. I look around. The decor is nice at least, and the vibe gets better when the song changes to someting more... me."

        "I watch the other people while I sway back and forth slightly in my seat. The dance floor is a frenetic morass of lust and sweat and body heat. It smells {i}delicious{/i}."

        beast "It sure does. Why not go fishing in that pond?"

        "Because I want to see what's on tap, so to speak. I watch and wait."

        if pc.hasDisciplinePower(_presence, PRES_AWE):
            "And now I'm tired of waiting, so I spread my aura out to speed things along. I could already feel a few sets of eyes running me up and down, but now every head in the vicinity is turned."
        else:
            "I wait for a few heads to turn. A few sets of eyes running me up and down."

        "A big woman in black jeans and one of those leather jackets that comes pre-scuffed sits down next to me. She's got a side-parted bob that looks like a hairstylist worked very hard to make it seem unkempt in a way that just happened to be attractive."

        "And she {i}is{/i} attractive. She's tall and stocky with a dimpled chin and a broad, sunny smile. Big eyes, big arms, big boobs, big everything. Her style is poseur as fuck, but who am I to judge someone else for being inauthentic?"

        beast "Yeah, you lie about literally everything."

        "She's actually really charming. Funny too. I find myself paying attention to her out of genuine interest, not just to satisfy my feeding requirements. She clearly comes from money, though she downplays it and tries to avoid mentioning her family."

        "She's been a whole lot of places and she has a story for every one. Shit, I've only ever been outside the country twice, visiting family in Davao as a kid. Not like I could go back there now. I should have studied abroad when I had the chance."

        beast "Focus, [petname]. You have a whole-ass eternity to regret your many mistakes. Right now it's lunchtime. Get on with it."

        "Fine. I give her the doe-eyes and she asks me to dance. I joke that I thought she'd never ask. And she's not bad. She's got wandering hands, but I don't mind. A slow song comes on - a downtempo remix of some old 70s soul ballad."

        "I can't quite place it, but it's familiar. I can remember my Dad dancing to it and I'm pretty sure Kanye has sampled it. Her arms encircle me, and I feel content in a way that I haven't in years."

        "For a fleeting moment I desperately wish I could go on a real date. Have actual human relationships again. Have a friend or a lover that isn't under the influence of my Blood. That I'm not preying on or stealing life from."

        beast "That went badly when you were a living human being. How do you think it would go now that you're a corpse? Focus! We. Need. Blood."

        "Fuck off. I don't need you to tell me any of that. The Hunger gnaws at me, killing the mood. I whisper in her ear, and in a few minutes we're out and back at her place."

        "She's bigger and stronger than a lot of the men I've been with. Her mouth tastes like wine and her scent is intoxicating. She's not wearing perfume and there's only the slightest hint of body wash. She's holding me up with one arm and the other has already got my shirt off. I wrap my legs around her as we fall to the bed."

        beast "What's taking you so goddamn long? Drink her already."

        "I ignore the Beast for as long as I can. I want her like I'm still alive, and I don't let my fangs slide out until she's howling into my chest with my hand between her thighs. Then I bite her lip as I kiss her one final time."

        $ pc.soundFeed()

        beast "You really like this one, don't you? Why not keep her?"

        "This again? For the last time, you and I both know that's now how it-"

        beast "I mean ghoul her, you imbecile."

        "I stop feeding. She sighs and smiles, sated and delirious."

        $ pc.slakeHunger(3)

        if story_ghouled_ex:
            "You can't be serious. I just got done ghouling someone I really, {i}really{/i} shouldn't have."

            beast "So what have you got to lose, then?"
        elif story_met_ex:
            "Are you fucking insane? With my ex lurking about? With everything else going on?"

            beast "Haven't you noticed that this whole city's in chaos? Everyone important is distracted. If you want to do something bold, there's no better time."
        else:
            "...What? No. That's insane."

            beast "Yes, it is. But so is a lot else of what you've done lately."

        beast "Listen. I'm trying to help you. I mean, I'm trying to help me. But by way of helping you. Your emotional instability is distracting you from the hunt, from your job, from everything that's actually important."

        beast "We can't keep going on like this. And I understand hunger. I {i}am{/i} hunger. So if you hunger for love, make some. Or take some. Whatever; I don't care. Just claim what you want and be satisfied, for fuck's sake!"

        beast "You're a vampire! A Ventrue! We don't pine, we don't long, and we don't wallow in regret. If we want something, we take it or we make it. You obviously want her, so take her. Then make her, into whatever it is you want out of her."

        beast "Then we can finally focus on what matters!"

        "..."

        "I... no. I hear you. But no. I won't ruin this woman's life. I'll... I'll focus from now on. Just... let's go. Please."

        beast "I'll hold you to that, [petname]."

        jump feeding.hx_srn_win



        label .hx_srn_generic:

            $ grade = evalt(pc.basictest(hunting_difficulty, _cha, _intr))

            if grade == SUCCESS or grade == MESSYCRIT:
                if story_this_time == SIREN_WOMEN:
                    "I hit one of the spots on [ghoulname]'s list. Great music, great vibe."

                    "I talk to a lot of pretty girls, laughing and dancing with them. Listening to the stories they have to tell. One woman is clearly the most interested, so I spend the rest of the night with her."

                    "We hit a couple more clubs, then a restaurant (where I make excuses for not eating anything), and finally end up back at her apartment."

                    $ pc.soundFeed("It's a great night, and we both end up satisfied. I watch her sleep contentedly for a few minutes before I grab my things and go.")
                    $ pc.slakeHunger(2)
                else:
                    "I sit down at the bar in one of [ghoulname]'s recommended places. It doesn't take long for men to start approaching me. It takes a while to get through all the fuckboys who think they've got game and find a guy willing to actually sit and talk for a bit before we fuck."

                    "But eventually I find a guy with a sad story that fits my type to a T. And he's good-looking, so I drop hints until he asks me if I want to get out of here."

                    $ pc.soundFeed("And then, we both get what we want. I check his pulse and breathing before putting my clothes back on and leaving.")
                    $ pc.slakeHunger(2)

                jump feeding.hx_srn_win
            else:
                "I hit club after club, and there's plenty of interest."

                "But there's no one that fits my requirements. Or at least, no one with a \"tell\" that I can pick up on."

                "This isn't good. Am I losing my touch? Usually I'm pretty good at getting people to open up."

                beast "..."

                beast "You're {i}really{/i} not going to like what happens if you keep screwing up like this."

                jump feeding.hx_srn_fail

        label .hx_srn_win: # SIREN NORMAL SUCCESS STATE

            scene black with fade

            "..."

            $ pc.soundRoadTrip()
            play music audio.huntsuccess
            scene bg driving road2

            "Well that... happened."

            beast "Mediocre success is yours once again. Sure would be nice if you cared more about eating our food than fucking it."

            "...That's vile, even for you."

            beast "You don't know the half of it."

            beast "...Well, actually I guess you do."

            stop music fadeout 2.0
            scene black with fade

            $ updateTime(0.5)
            return

        label .hx_srn_fail: # SIREN GENERIC FAILURE STATE

            $ updateTime(0.5)
