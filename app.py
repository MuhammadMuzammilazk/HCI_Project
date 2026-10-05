import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="A Little Something",
    page_icon="✨",
    layout="centered"
)


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "start"

if "seen_surprises" not in st.session_state:
    st.session_state.seen_surprises = set()

if "memory_choice" not in st.session_state:
    st.session_state.memory_choice = None

if "gift_stage" not in st.session_state:
    st.session_state.gift_stage = 0

if "final_image" not in st.session_state:
    st.session_state.final_image = False

if "last_confetti_page" not in st.session_state:
    st.session_state.last_confetti_page = None

# =========================================================
# MUSIC
# =========================================================

SONG_FILE = Path(__file__).parent / "birthday.mp3"


def play_background_music():

    if not SONG_FILE.exists():
        return

    audio_b64 = base64.b64encode(
        SONG_FILE.read_bytes()
    ).decode("ascii")

    components.html(
        f"""
        <audio
            id="birthday-music"
            preload="auto"
            loop
            muted
        >
            <source
                src="data:audio/mpeg;base64,{audio_b64}"
                type="audio/mpeg"
            >
        </audio>

        <script>

        const audio =
            document.getElementById("birthday-music");

        if (audio) {{

            audio.volume = 0.45;

            const savedTime =
                sessionStorage.getItem(
                    "birthday_music_time"
                );

            let restored = false;


            function saveMusicTime() {{

                try {{

                    if (
                        audio &&
                        Number.isFinite(audio.currentTime)
                    ) {{

                        sessionStorage.setItem(
                            "birthday_music_time",
                            audio.currentTime.toString()
                        );

                    }}

                }} catch (e) {{}}

            }}


            function restoreAndPlay() {{

                if (restored) {{
                    return;
                }}

                restored = true;

                try {{

                    if (savedTime) {{

                        const time =
                            parseFloat(savedTime);

                        if (
                            Number.isFinite(time) &&
                            time >= 0 &&
                            time < audio.duration
                        ) {{

                            audio.currentTime = time;

                        }}

                    }}

                }} catch (e) {{}}


                audio.muted = false;

                audio.play().catch(() => {{}});

            }}


            if (audio.readyState >= 1) {{

                restoreAndPlay();

            }} else {{

                audio.addEventListener(
                    "loadedmetadata",
                    restoreAndPlay,
                    {{once:true}}
                );

            }}


            audio.addEventListener(
                "timeupdate",
                saveMusicTime
            );


            window.addEventListener(
                "pagehide",
                saveMusicTime
            );


            window.addEventListener(
                "beforeunload",
                saveMusicTime
            );


            document.addEventListener(
                "click",
                () => {{

                    if (audio.paused) {{

                        audio.play().catch(() => {{}});

                    }}

                }},
                {{once:false}}
            );

        }}

        </script>
        """,
        height=0,
        scrolling=False
    )

# =========================================================
# PAGE CELEBRATION
# =========================================================

def page_celebration():

    if (
        st.session_state.last_confetti_page
        != st.session_state.page
    ):

        st.balloons()

        st.session_state.last_confetti_page = (
            st.session_state.page
        )


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       MAIN APP
       ===================================================== */

    .stApp {

        background:
            radial-gradient(
                circle at 15% 10%,
                rgba(110,70,255,.28),
                transparent 30%
            ),

            radial-gradient(
                circle at 85% 85%,
                rgba(0,190,255,.18),
                transparent 30%
            ),

            radial-gradient(
                circle at 50% 45%,
                rgba(180,70,255,.08),
                transparent 35%
            ),

            linear-gradient(
                135deg,
                #070914 0%,
                #0c1020 50%,
                #080b16 100%
            );

        color:#fff !important;

        min-height:100vh;
    }


    .block-container {

        max-width:900px;

        padding-top:45px;
        padding-bottom:80px;

        animation:pageEnter .7s ease-out;
    }


    /* =====================================================
       PAGE ANIMATION
       ===================================================== */

    @keyframes pageEnter {

        0% {
            opacity:0;
            transform:translateY(25px);
        }

        100% {
            opacity:1;
            transform:translateY(0);
        }

    }


    @keyframes fadeUp {

        0% {
            opacity:0;
            transform:translateY(30px) scale(.98);
        }

        100% {
            opacity:1;
            transform:translateY(0) scale(1);
        }

    }


    @keyframes floating {

        0%,100% {
            transform:translateY(0);
        }

        50% {
            transform:translateY(-10px);
        }

    }


    @keyframes glowPulse {

        0%,100% {

            box-shadow:
                0 0 20px rgba(130,90,255,.18),
                0 0 50px rgba(80,120,255,.05);

        }

        50% {

            box-shadow:
                0 0 35px rgba(150,100,255,.38),
                0 0 80px rgba(80,130,255,.12);

        }

    }


    /* =====================================================
       TITLES
       ===================================================== */

    .title {

        text-align:center;

        font-size:54px;

        font-weight:900;

        margin-top:80px;

        color:#fff !important;

        text-shadow:
            0 0 18px rgba(150,110,255,.55),
            0 0 45px rgba(80,120,255,.20);

        animation:
            fadeUp 1s ease-out,
            floating 4s ease-in-out infinite;
    }


    .subtitle {

        text-align:center;

        font-size:21px;

        color:#dfe5f5 !important;

        margin-top:22px;

        line-height:1.8;

        animation:fadeUp 1.2s ease-out;
    }


    .screen-title {

        text-align:center;

        font-size:39px;

        font-weight:850;

        margin-top:65px;

        color:#fff !important;

        text-shadow:
            0 0 24px rgba(130,120,255,.28);

        animation:fadeUp .8s ease-out;
    }


    .screen-text {

        text-align:center;

        font-size:20px;

        color:#dfe5f5 !important;

        line-height:1.9;

        margin-top:26px;

        animation:fadeUp 1s ease-out;
    }


    .emoji {

        text-align:center;

        font-size:62px;

        margin-top:50px;

        animation:
            floating 3s ease-in-out infinite;
    }


    .birthday-title {

        text-align:center;

        font-size:51px;

        font-weight:950;

        margin-top:22px;

        color:#fff !important;

        text-shadow:
            0 0 12px rgba(255,100,190,.65),
            0 0 35px rgba(110,100,255,.50);

        animation:fadeUp 1s ease-out;
    }


    .birthday-text {

        text-align:center;

        font-size:22px;

        color:#e7ebf8 !important;

        line-height:1.9;

        margin-top:28px;

        animation:fadeUp 1.2s ease-out;
    }


    /* =====================================================
       CARDS
       ===================================================== */

    .card {

        background:
            linear-gradient(
                135deg,
                rgba(255,255,255,.07),
                rgba(255,255,255,.025)
            );

        border:1px solid rgba(255,255,255,.13);

        border-radius:20px;

        padding:28px 24px;

        margin-top:25px;

        text-align:center;

        box-shadow:
            0 12px 35px rgba(0,0,0,.25);

        backdrop-filter:blur(12px);

        animation:cardReveal .7s ease-out;

        transition:
            transform .25s ease,
            box-shadow .25s ease;
    }


    .card:hover {

        transform:translateY(-5px);

        box-shadow:
            0 18px 45px rgba(80,70,200,.25);
    }


    @keyframes cardReveal {

        0% {

            opacity:0;

            transform:
                translateY(25px)
                scale(.97);
        }

        100% {

            opacity:1;

            transform:
                translateY(0)
                scale(1);
        }

    }


    .card-title {

        font-size:25px;

        font-weight:800;

        color:#fff !important;

        margin-bottom:12px;
    }


    .card-text {

        font-size:18px;

        line-height:1.8;

        color:#d9e0f0 !important;
    }


    /* =====================================================
       FINAL BOX
       ===================================================== */

    .final-box {

        text-align:center;

        background:
            linear-gradient(
                135deg,
                rgba(116,76,255,.16),
                rgba(0,190,255,.08)
            );

        border:1px solid rgba(255,255,255,.14);

        border-radius:28px;

        padding:38px 28px;

        margin-top:45px;

        box-shadow:
            0 18px 55px rgba(0,0,0,.30);

        animation:
            fadeUp 1.2s ease-out,
            glowPulse 5s ease-in-out infinite;
    }


    .final-title {

        font-size:42px;

        font-weight:900;

        color:#fff !important;

        text-shadow:
            0 0 22px rgba(150,100,255,.4);
    }


    .final-text {

        font-size:19px;

        color:#dfe5f5 !important;

        line-height:2;

        margin-top:22px;
    }


    /* =====================================================
       MEMORY BREAK BUTTON
       ===================================================== */

    .broken-button {

        margin:25px auto 10px;

        max-width:520px;

        padding:17px 25px;

        border:2px dashed rgba(255,255,255,.35);

        border-radius:14px;

        color:#8f97aa;

        font-size:17px;

        font-weight:750;

        text-decoration:line-through;

        opacity:.62;

        animation:
            breakShake .75s ease-in-out;
    }


    @keyframes breakShake {

        0% {
            transform:translateX(0) rotate(0);
        }

        20% {
            transform:translateX(-10px) rotate(-3deg);
        }

        40% {
            transform:translateX(10px) rotate(3deg);
        }

        60% {
            transform:translateX(-7px) rotate(-2deg);
        }

        80% {
            transform:translateX(7px) rotate(2deg);
        }

        100% {
            transform:translateX(0) rotate(0);
        }

    }


    /* =====================================================
       GIFT
       ===================================================== */

    .gift-link {

        position:fixed;

        z-index:99999;

        width:120px;

        height:120px;

        display:flex;

        align-items:center;

        justify-content:center;

        text-decoration:none !important;

        font-size:82px;

        line-height:1;

        border-radius:30px;

        filter:
            drop-shadow(
                0 0 25px rgba(170,100,255,.65)
            );

        animation:
            giftFloat 2.5s ease-in-out infinite;
    }


    .gift-center {

        left:50%;

        top:50%;

        transform:
            translate(-50%,-50%);
    }


    .gift-right-bottom {

        right:25px;

        bottom:25px;
    }


    .gift-left-top {

        left:25px;

        top:25px;
    }


    .gift-link:hover {

        transform:
            scale(1.10);
    }


    @keyframes giftFloat {

        0%,100% {

            margin-top:0;
        }

        50% {

            margin-top:-12px;
        }

    }


    /* =====================================================
       GIFT FOUND
       ===================================================== */

    .gift-open {

        text-align:center;

        font-size:115px;

        filter:
            drop-shadow(
                0 0 30px rgba(255,190,80,.65)
            );

        animation:
            giftOpen 1s ease-out,
            floating 3s ease-in-out infinite;
    }


    @keyframes giftOpen {

        0% {

            opacity:0;

            transform:
                scale(.3)
                rotate(-15deg);
        }

        60% {

            opacity:1;

            transform:
                scale(1.2)
                rotate(5deg);
        }

        100% {

            transform:
                scale(1)
                rotate(0);
        }

    }


    /* =====================================================
       BUTTONS
       ===================================================== */

    .stButton > button {

        width:100%;

        min-height:50px;

        border-radius:14px;

        border:
            1px solid rgba(255,255,255,.16);

        background:
            linear-gradient(
                135deg,
                #6848ee,
                #9658f5
            );

        color:#fff !important;

        font-size:17px;

        font-weight:750;

        padding:12px 18px;

        box-shadow:
            0 9px 28px rgba(80,50,190,.32);

        transition:
            all .22s ease;
    }


    .stButton > button:hover {

        transform:
            translateY(-3px)
            scale(1.01);

        border-color:
            rgba(255,255,255,.35);

        box-shadow:
            0 13px 34px rgba(100,70,230,.48);
    }


    .stButton > button:active {

        transform:scale(.96);
    }


    .stButton > button p {

        color:#fff !important;
    }


    /* =====================================================
       MOBILE
       ===================================================== */
/* =====================================================
   STREAMLIT GIFT BUTTON FIX
   ===================================================== */

body:has(.gift-stage-0) .stButton {
    position:fixed !important;
    left:50% !important;
    top:50% !important;
    width:120px !important;
    height:120px !important;
    transform:translate(-50%,-50%) !important;
    z-index:99999 !important;
    margin:0 !important;
}

body:has(.gift-stage-1) .stButton {
    position:fixed !important;
    right:25px !important;
    bottom:25px !important;
    width:120px !important;
    height:120px !important;
    z-index:99999 !important;
    margin:0 !important;
}

body:has(.gift-stage-2) .stButton {
    position:fixed !important;
    left:25px !important;
    top:25px !important;
    width:120px !important;
    height:120px !important;
    z-index:99999 !important;
    margin:0 !important;
}

body:has(.gift-stage-0) .stButton > button,
body:has(.gift-stage-1) .stButton > button,
body:has(.gift-stage-2) .stButton > button {

    width:120px !important;
    height:120px !important;

    min-height:120px !important;

    padding:0 !important;

    border:none !important;

    border-radius:30px !important;

    background:transparent !important;

    box-shadow:none !important;

    font-size:82px !important;

    line-height:1 !important;

    transition:
        transform .25s ease,
        filter .25s ease !important;

    animation:
        giftFloat 2.5s ease-in-out infinite !important;
}

body:has(.gift-stage-0) .stButton > button:hover,
body:has(.gift-stage-1) .stButton > button:hover,
body:has(.gift-stage-2) .stButton > button:hover {

    transform:scale(1.10) !important;

    filter:
        drop-shadow(
            0 0 25px rgba(170,100,255,.65)
        ) !important;
}

body:has(.gift-stage-0) .stButton > button p,
body:has(.gift-stage-1) .stButton > button p,
body:has(.gift-stage-2) .stButton > button p {

    font-size:82px !important;
    line-height:1 !important;
    margin:0 !important;
}

    @media(max-width:700px) {

        .title {

            font-size:40px;

            margin-top:55px;
        }


        .screen-title {

            font-size:31px;
        }


        .birthday-title {

            font-size:38px;
        }


        .screen-text,
        .birthday-text {

            font-size:18px;
        }


        .final-title {

            font-size:32px;
        }


        .final-text {

            font-size:17px;
        }


        .gift-link {

            width:90px;

            height:90px;

            font-size:65px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PAGE ENTER CELEBRATION
# =========================================================

page_celebration()


# =========================================================
# BACKGROUND MUSIC
# =========================================================

if st.session_state.page != "start":

    play_background_music()


# =========================================================
# PAGE 1 — START
# =========================================================

if st.session_state.page == "start":

    st.markdown(
        '<div class="title">Hey, BRO.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
        Don't Leave!!

        Firstly just take a look what i pulled!!
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    _, col2, _ = st.columns([1,2,1])

    with col2:

        if st.button(
            "Let's Begin",
            use_container_width=True
        ):

            st.session_state.page = "story"

            st.rerun()


# =========================================================
# PAGE 2 — STORY
# =========================================================

elif st.session_state.page == "story":

    st.markdown(
        """
        <div class="screen-title">

        It's been a while na?.

        </div>

        <div class="screen-text">
        We probably don't expect much now.

        That's okay.

        Just keep going for few more!!.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    _, col2, _ = st.columns([1,2,1])

    with col2:

        if st.button(
            "Continue",
            use_container_width=True
        ):

            st.session_state.page = "memory"

            st.rerun()


# =========================================================
# PAGE 3 — MEMORY
# =========================================================

elif st.session_state.page == "memory":

    st.markdown(
        """
        <div class="screen-title">

        Do you remember ?

        </div>

        <div class="screen-text">
        What we used to do?

        The Convos!

        Actually Leave it!

        Go Ahead>>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")


    if st.session_state.memory_choice == "no":

        st.markdown(
            """
            <div class="broken-button">

            NO I DO NOT REMEMBER

            </div>

            <div class="screen-text">

            <b>Nice try.</b>

            That button just broke.

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        _, col2, _ = st.columns([1,2,1])

        with col2:

            if st.button(
                "I REMEMBER",
                use_container_width=True
            ):

                st.session_state.memory_choice = "yes"

                st.session_state.page = "nostalgia"

                st.rerun()


    else:

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "I REMEMBER",
                use_container_width=True
            ):

                st.session_state.memory_choice = "yes"

                st.session_state.page = "nostalgia"

                st.rerun()


        with col2:

            if st.button(
                "NO I DO NOT REMEMBER",
                use_container_width=True
            ):

                st.session_state.memory_choice = "no"

                st.rerun()


# =========================================================
# PAGE 4 — NOSTALGIA
# =========================================================

elif st.session_state.page == "nostalgia":

    st.markdown(
        """
        <div class="screen-title">

        Yeah Obviously you do

        </div>

        <div class="screen-text">
        Maybe that's the strange thing about memories.

        You don't realize they're important until they're already memories.

        Anyway................

        There's a reason you're still clicking.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    _, col2, _ = st.columns([1,2,1])

    with col2:

        if st.button(
            "Let's See Why",
            use_container_width=True
        ):

            st.session_state.page = "birthday"

            st.rerun()


# =========================================================
# PAGE 5 — BIRTHDAY
# =========================================================

elif st.session_state.page == "birthday":

    st.markdown(
        """
        <div class="emoji">

        🎂 🎉 🎈

        </div>

        <div class="birthday-title">

        HAPPY BIRTHDAY, BRO!!!!!!!!!!!!!!!.

        </div>

        <div class="birthday-text">

        Umm! I don't know jjust felt i should so....
        
        ↓ I DID

        Not a long message.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    _, col2, _ = st.columns([1,2,1])

    with col2:

        if st.button(
            "Open Your Birthday Wish",
            use_container_width=True
        ):

            st.session_state.page = "gift"

            st.session_state.gift_stage = 0

            st.rerun()


# =========================================================
# PAGE 6 — GIFT HUNT
# =========================================================

elif st.session_state.page == "gift":

    # =====================================================
    # NO EXTRA TEXT
    # =====================================================

    # Only the gift appears on this page.
    # No "One Last Thing..."
    # No "Before you continue..."
    # No "You have to find it."


    # =====================================================
    # GIFT — CENTER
    # =====================================================

    if st.session_state.gift_stage == 0:

        st.markdown(
            '<div class="gift-stage-0"></div>',
            unsafe_allow_html=True
        )

        if st.button(
            "🎁",
            key="gift_center",
            use_container_width=False
        ):

            st.session_state.gift_stage = 1

            st.rerun()


    # =====================================================
    # GIFT — BOTTOM RIGHT
    # =====================================================

    elif st.session_state.gift_stage == 1:

        st.markdown(
            '<div class="gift-stage-1"></div>',
            unsafe_allow_html=True
        )

        if st.button(
            "🎁",
            key="gift_bottom_right",
            use_container_width=False
        ):

            st.session_state.gift_stage = 2

            st.rerun()


    # =====================================================
    # GIFT — TOP LEFT
    # =====================================================

    elif st.session_state.gift_stage == 2:

        st.markdown(
            '<div class="gift-stage-2"></div>',
            unsafe_allow_html=True
        )

        if st.button(
            "🎁",
            key="gift_top_left",
            use_container_width=False
        ):

            st.session_state.gift_stage = 3

            st.session_state.page = "wish"

            st.session_state.gift_stage = 0

            st.rerun()


# =========================================================
# PAGE 7 — LONG BIRTHDAY WISH
# =========================================================

elif st.session_state.page == "wish":

    st.markdown(
        """
        <div class="screen-title">

        Happy Birthday, BRO.

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="screen-text" style="text-align:left;">

        Another year added to your story.

        I won't give you the usual birthday wishes about happiness, success, and everything else people say because they have to.

        I'll just say this:

        <b>I hope the life ahead of you feels worth living.</b>

        Not perfect.

        Not easy every day.

        Just meaningful enough that, when you look back, you feel like it was all worth it.

        I hope you find things that genuinely matter to you.

        Things that give you a reason to wake up in the morning.

        Things that make even the difficult days a little easier to get through.

        I hope you meet people you never have to pretend around.

        People you can trust without questioning where you stand with them.

        People who stay, not only when life is easy, but also when things get complicated.

        I hope you find work you're proud of.

        Something that gives you more than just a paycheck.

        Something that makes you feel like you're building a life that truly belongs to you.

        I hope you experience the kind of happiness that doesn't need to be shown to everyone.

        The quiet kind.

        The kind you feel during a good conversation, a peaceful evening, a random laugh, or a moment when you realize that life is slowly becoming what you hoped it would be.

        I hope you never get so busy growing up that you forget to enjoy being alive.

        There will be difficult days.

        Some things won't work out.

        People will leave.

        Plans will change.

        Some years will feel heavier than others.

        But I hope you always find your way back to yourself.

        I hope you have the courage to walk away from what no longer feels right, the patience to wait for what takes time, and the strength to keep going when the road gets difficult.

        I hope you don't measure your life only by achievements.

        Some of the best moments won't come with awards, promotions, or anything you can put on a resume.

        Sometimes, they'll just be memories.

        Late-night conversations.

        Random plans.

        Unplanned moments.

        Inside jokes that make no sense to anyone else.

        People who slowly become important without you even realizing when it happened.

        I hope you collect a lot of those moments.

        And years from now, when another birthday comes around, I hope you can look at the person you've become and feel proud of him.

        Not because he had everything figured out, but because he kept moving forward.

        Because he stayed kind.

        Because he didn't give up on himself.

        Because he learned.

        Because he grew.

        Because he kept choosing to move forward, even when life wasn't always kind to him.

        So yeah...

        <b>Happy Birthday, BRO.</b>

        I hope this next chapter brings you closer to the person you truly want to become.

        I hope there are more good days than bad ones.

        More reasons to smile than reasons to worry.

        More moments you'll remember years from now.

        And above everything else,

        <b>I hope the life ahead of you feels worth living.</b>

        That's all I really wish for you.

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    _, col2, _ = st.columns([1,2,1])

    with col2:

        if st.button(
            "There's More",
            use_container_width=True
        ):

            st.session_state.page = "surprises"

            st.rerun()


# =========================================================
# PAGE 8 — FOUR SURPRISES
# =========================================================

elif st.session_state.page == "surprises":

    st.markdown(
        """
        <div class="screen-title">

        You made it this far.

        </div>

        <div class="screen-text">

        So I left four things here for you.

        They're small.

        But each one means something.

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")


    c1, c2 = st.columns(2)


    with c1:

        if st.button(
            "No More Disturbance",
            use_container_width=True
        ):

            st.session_state.seen_surprises.add(
                "disturbance"
            )

            st.rerun()


    with c2:

        if st.button(
            "Always Available",
            use_container_width=True
        ):

            st.session_state.seen_surprises.add(
                "available"
            )

            st.rerun()


    st.write("")


    c3, c4 = st.columns(2)


    with c3:

        if st.button(
            "For The Best",
            use_container_width=True
        ):

            st.session_state.seen_surprises.add(
                "best"
            )

            st.rerun()


    with c4:

        if st.button(
            "The Final Wish",
            use_container_width=True
        ):

            st.session_state.seen_surprises.add(
                "final_wish"
            )

            st.rerun()


    if "disturbance" in st.session_state.seen_surprises:

        st.markdown(
            """
            <div class="card">

            <div class="card-title">

            No More Disturbance

            </div>

            <div class="card-text">

            I won't disturb your peace anymore, and maybe this is the last time I say these things — but just because I step back doesn't mean I stopped caring.

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    if "available" in st.session_state.seen_surprises:

        st.markdown(
            """
            <div class="card">

            <div class="card-title">

            Always Available

            </div>

            <div class="card-text">

            You may not hear from me anymore, but if life ever gets heavy, remember that somewhere, somehow, I'm still there — no questions, no expectations, just a person you can reach whenever you need someone.

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    if "best" in st.session_state.seen_surprises:

        st.markdown(
            """
            <div class="card">

            <div class="card-title">

            For The Best

            </div>

            <div class="card-text">

            Maybe some of the things that happened between us weren't good, and maybe they hurt more than either of us expected — but perhaps some endings aren't meant to punish us; perhaps they happen because life knows a better road is waiting somewhere ahead.

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    if "final_wish" in st.session_state.seen_surprises:

        st.markdown(
            """
            <div class="card">

            <div class="card-title">

            The Final Wish

            </div>

            <div class="card-text">

            More than happiness, success, or anything else, I hope you find a life that feels peaceful when you're alone with your thoughts — a life where your heart feels light, your people feel real, and one day you look back and quietly realize that everything you lost, everything you survived, and everything you became was somehow worth it.

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    if len(st.session_state.seen_surprises) == 4:

        st.markdown(
            """
            <div class="screen-text">
            You found all four. 👀

            Okay... now there's only one last thing
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        _, col2, _ = st.columns([1,2,1])

        with col2:

            if st.button(
                "Lets go to the end",
                use_container_width=True
            ):

                st.session_state.page = "final"

                st.rerun()


# =========================================================
# PAGE 9 — FINAL
# =========================================================

elif st.session_state.page == "final":

    st.markdown(
        """
        <div class="final-box">

        <div class="final-title">

        That's it, BRO.

        </div>

        <div class="final-text">

        No gift.

        No long speech.

        No expectations.

        Just a few words from someone

        who once shared a small part of your life

        and still remembers it with respect.

        Maybe some chapters aren't meant to continue.

        Maybe some people are only meant to be a part of a certain time,

        and then quietly become a memory.

        And that's okay.

        I don't want to disturb your peace anymore.

        I don't want anything from you.

        I just wanted, for once, to leave something behind

        that doesn't ask for a reply.

        Whatever happened between us wasn't always good.

        Some things hurt.

        Some things changed.

        But with time, I've started believing

        that maybe they happened for a reason.

        Maybe some endings are necessary

        before better things can begin.

        So I'll leave this here.

        Not as a goodbye filled with sadness,

        but as a quiet thank you

        for the memories that were good while they lasted.

        I genuinely hope life is kind to you.

        I hope you find people who value you,

        places where you feel at peace,

        and a life that makes you grateful

        for the person you've become.

        And if life ever gets difficult,

        just remember that even if I don't show up anymore,

        I'll always be someone you can reach.

        No expectations.

        No questions.

        Just there.

        <br><br>

        <b>Happy Birthday, Saad.</b>

        Take care of yourself.

        And I hope, wherever life takes you from here,

        it takes you somewhere good.

        <br><br>

        — <b>BRO</b>

        <i>

        Some memories are better left untouched,

        not because they meant nothing,

        but because they meant enough.

        </i>

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")


    if not st.session_state.final_image:

        _, col2, _ = st.columns([1,2,1])

        with col2:

            if st.button(
                "One Last Thing",
                use_container_width=True
            ):

                st.session_state.final_image = True

                st.rerun()


    else:

        image_file = None

        image_folder = Path(__file__).parent


        for filename in [
            "SISI.png",
            "SISI.jpg",
            "SISI.jpeg",
            "sisi.png",
            "sisi.jpg",
            "sisi.jpeg"
        ]:

            candidate = image_folder / filename

            if candidate.exists():

                image_file = candidate

                break


        st.markdown(
            """
            <div class="screen-text">

            JUST EXTRA!!!

            </div>
            """,
            unsafe_allow_html=True
        )


        if image_file is not None:

            st.image(
                str(image_file),
                use_container_width=True
            )


        else:

            st.markdown(
                """
                <div class="card">

                <div class="card-title">

                Your final gift is waiting.

                </div>

                <div class="card-text">

                Put your image in the HCI_Project folder and name it SISI.png, SISI.jpg, or SISI.jpeg.

                </div>

                </div>
                """,
                unsafe_allow_html=True
            )