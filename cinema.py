import streamlit as st
import time
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="PRASÉ CINEMA",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# MOVIE DATA
# =========================================================

movies = {
    "🔥 Avengers: Endgame": {
        "price": 220,
        "image": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=900&q=80",
        "genre": "Action • Adventure",
        "rating": "9.2/10"
    },

    "🚀 Interstellar": {
        "price": 200,
        "image": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?auto=format&fit=crop&w=900&q=80",
        "genre": "Sci-Fi • Drama",
        "rating": "9.0/10"
    },

    "🦇 The Batman": {
        "price": 180,
        "image": "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?auto=format&fit=crop&w=900&q=80",
        "genre": "Action • Crime",
        "rating": "8.8/10"
    },

    "🌌 Avatar": {
        "price": 250,
        "image": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?auto=format&fit=crop&w=900&q=80",
        "genre": "Fantasy • Adventure",
        "rating": "8.7/10"
    }
}


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap'
);

/* =====================================================
   MAIN BACKGROUND
   ===================================================== */

.stApp {

    background:

        radial-gradient(
            circle at 10% 10%,
            rgba(229, 9, 20, 0.20),
            transparent 30%
        ),

        radial-gradient(
            circle at 90% 90%,
            rgba(255, 0, 0, 0.10),
            transparent 30%
        ),

        #070707;

    color: white;
}


/* =====================================================
   GLOBAL FONT
   ===================================================== */

* {
    font-family: 'Poppins', sans-serif;
}


.block-container {

    max-width: 1450px;

    padding-top: 2rem;

    padding-bottom: 4rem;
}


/* =====================================================
   LOGO
   ===================================================== */

.logo {

    text-align: center;

    font-family: 'Cinzel', serif;

    font-size: 68px;

    font-weight: 700;

    letter-spacing: 12px;

    color: #ff1e2d;

    animation: cinemaGlow 2s infinite alternate;

}


@keyframes cinemaGlow {

    from {

        text-shadow:
        0 0 5px #ff1e2d;

    }

    to {

        text-shadow:
        0 0 15px #ff1e2d,
        0 0 35px #e50914,
        0 0 55px #8b0000;

    }

}


.tagline {

    text-align: center;

    color: #cfcfcf;

    letter-spacing: 6px;

    font-size: 13px;

}


/* =====================================================
   RED LINE
   ===================================================== */

.red-line {

    height: 2px;

    margin: 25px 0;

    background:

        linear-gradient(
            90deg,
            transparent,
            #e50914,
            #ff4b55,
            #e50914,
            transparent
        );
}


/* =====================================================
   SECTION TITLE
   ===================================================== */

.section-title {

    font-family: 'Cinzel', serif;

    color: #ff3b48;

    font-size: 28px;

    margin-bottom: 20px;

}


/* =====================================================
   MOVIE CARD
   ===================================================== */

.movie-card {

    background:

        linear-gradient(
            145deg,
            rgba(255,255,255,0.10),
            rgba(255,255,255,0.02)
        );

    border:

        1px solid
        rgba(229,9,20,0.30);

    border-radius: 20px;

    padding: 18px;

    margin-bottom: 10px;

    transition:

        transform 0.35s ease,

        box-shadow 0.35s ease,

        border-color 0.35s ease;

}


.movie-card:hover {

    transform:

        translateY(-10px)
        scale(1.02);

    border-color:

        #ff1e2d;

    box-shadow:

        0 20px 50px
        rgba(229,9,20,0.25);

}


/* =====================================================
   MOVIE TITLE
   ===================================================== */

.movie-name {

    font-size: 20px;

    font-weight: 700;

    color: white;

}


.movie-info {

    color: #aaa;

    font-size: 14px;

    margin-top: 5px;

}


.movie-price {

    color: #ff3b48;

    font-size: 20px;

    font-weight: 700;

    margin-top: 8px;

}


/* =====================================================
   BOOKING BOX
   ===================================================== */

.booking-box {

    background:

        linear-gradient(
            145deg,
            #151515,
            #080808
        );

    border:

        1px solid
        rgba(229,9,20,0.35);

    border-radius: 25px;

    padding: 30px;

    box-shadow:

        0 20px 60px
        rgba(0,0,0,0.6);

}


/* =====================================================
   TICKET
   ===================================================== */

.ticket {

    background:

        linear-gradient(
            135deg,
            #1c1c1c,
            #090909
        );

    border:

        2px dashed
        #e50914;

    border-radius: 20px;

    padding: 30px;

    box-shadow:

        0 15px 50px
        rgba(229,9,20,0.15);

}


.ticket-title {

    text-align: center;

    font-family: 'Cinzel', serif;

    font-size: 30px;

    color: #ff3442;

}


/* =====================================================
   TOTAL
   ===================================================== */

.total-box {

    background:

        linear-gradient(
            90deg,
            #8b0000,
            #e50914,
            #ff4652,
            #e50914,
            #8b0000
        );

    color: white;

    padding: 20px;

    border-radius: 18px;

    text-align: center;

    font-size: 28px;

    font-weight: 700;

    animation: pulse 2s infinite;

}


@keyframes pulse {

    0% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.02);
    }

    100% {
        transform: scale(1);
    }

}


/* =====================================================
   BUTTON
   ===================================================== */

.stButton > button {

    background:

        linear-gradient(
            90deg,
            #8b0000,
            #e50914,
            #8b0000
        );

    color: white;

    border: none;

    border-radius: 30px;

    padding: 14px;

    font-weight: 700;

    transition: 0.3s;

}


.stButton > button:hover {

    transform: scale(1.04);

    box-shadow:

        0 0 30px
        rgba(229,9,20,0.50);

}


/* =====================================================
   SIDEBAR
   ===================================================== */

section[data-testid="stSidebar"] {

    background:

        linear-gradient(
            180deg,
            #120707,
            #050505
        );

    border-right:

        1px solid
        rgba(229,9,20,0.25);

}


/* =====================================================
   FOOTER
   ===================================================== */

.footer {

    text-align: center;

    color: #666;

    margin-top: 50px;

    letter-spacing: 3px;

    font-size: 12px;

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="logo">PRASÉ CINEMA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tagline">'
    'MOVIES • MEMORIES • MAGIC'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="red-line"></div>',
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🎬 PRASÉ CINEMA")

    st.markdown("### 👤 Guest Details")

    customer_name = st.text_input(
        "Customer Name",
        placeholder="Enter your name"
    )

    phone = st.text_input(
        "Mobile Number",
        placeholder="Enter mobile number"
    )

    st.markdown("---")

    st.markdown("### 🍿 Cinema Information")

    st.write("📍 PRASÉ Grand Cinemas")

    st.write("🕐 Open: 10:00 AM - 11:30 PM")

    st.write("🎞️ Premium Movie Experience")

    st.markdown("---")

    st.info(
        "🎬 Sit back, relax and enjoy your movie!"
    )


# =========================================================
# MOVIE SELECTION
# =========================================================

st.markdown(
    '<div class="section-title">'
    '🎬 NOW SHOWING'
    '</div>',
    unsafe_allow_html=True
)


movie_names = list(movies.keys())


selected_movie = st.selectbox(
    "🎥 Select Your Movie",
    movie_names
)


movie = movies[selected_movie]


# =========================================================
# MOVIE DISPLAY
# =========================================================

col1, col2 = st.columns([1, 1.5])


with col1:

    st.image(
        movie["image"],
        use_container_width=True
    )


with col2:

    st.subheader(selected_movie)

    st.write(
        f"🎭 **Genre:** {movie['genre']}"
    )

    st.write(
        f"⭐ **Rating:** {movie['rating']}"
    )

    st.markdown(
        f"### 🎟️ Starting from **₹{movie['price']}**"
    )

    st.success(
        "🔥 Limited seats available!"
    )
# =========================================================
# BOOKING DETAILS
# =========================================================

st.markdown(
    '<div class="red-line"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">'
    '🎟️ BOOK YOUR TICKETS'
    '</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


with col1:

    tickets = st.number_input(
        "🎟️ Number of Tickets",
        min_value=1,
        max_value=10,
        value=1,
        step=1
    )


with col2:

    ticket_type = st.selectbox(
        "💺 Ticket Category",
        [
            "Regular",
            "Premium",
            "VIP"
        ]
    )


with col3:

    show_date = st.date_input(
        "📅 Movie Date"
    )


# =========================================================
# TICKET PRICING
# =========================================================

ticket_extra = {

    "Regular": 0,

    "Premium": 80,

    "VIP": 160

}


ticket_price = (
    movie["price"]
    +
    ticket_extra[ticket_type]
)


ticket_total = (
    ticket_price * tickets
)


# =========================================================
# SHOW TIME
# =========================================================

show_time = st.selectbox(
    "🕐 Select Showtime",
    [
        "10:30 AM",
        "1:30 PM",
        "4:30 PM",
        "7:30 PM",
        "10:30 PM"
    ]
)


# =========================================================
# SEAT SECTION
# =========================================================

st.markdown(
    '<div class="section-title">'
    '💺 SELECT SEATS'
    '</div>',
    unsafe_allow_html=True
)


seat_options = [

    "A1", "A2", "A3", "A4",
    "B1", "B2", "B3", "B4",
    "C1", "C2", "C3", "C4",
    "D1", "D2", "D3", "D4"

]


selected_seats = st.multiselect(
    "Choose your seats",
    seat_options,
    max_selections=tickets
)


# =========================================================
# SNACKS
# =========================================================

st.markdown(
    '<div class="section-title">'
    '🍿 CINEMA SNACKS'
    '</div>',
    unsafe_allow_html=True
)


snack1, snack2, snack3 = st.columns(3)


with snack1:

    popcorn = st.checkbox(
        "🍿 Large Popcorn - ₹180"
    )


with snack2:

    drink = st.checkbox(
        "🥤 Large Cola - ₹120"
    )


with snack3:

    nachos = st.checkbox(
        "🧀 Nachos - ₹150"
    )


snack_total = 0


if popcorn:
    snack_total += 180


if drink:
    snack_total += 120


if nachos:
    snack_total += 150


# =========================================================
# DISCOUNT
# =========================================================

st.markdown(
    '<div class="red-line"></div>',
    unsafe_allow_html=True
)

coupon = st.text_input(
    "🎁 Discount Coupon",
    placeholder="Enter PRASÉ10 for 10% OFF"
)


discount = 0


if coupon.upper() == "PRASÉ10":

    discount = (
        ticket_total + snack_total
    ) * 0.10

    st.success(
        "🎉 Coupon applied! 10% discount."
    )

elif coupon:

    st.warning(
        "❌ Invalid coupon."
    )


# =========================================================
# GST
# =========================================================

subtotal = (
    ticket_total
    +
    snack_total
)


after_discount = (
    subtotal - discount
)


gst = (
    after_discount * 0.18
)


grand_total = (
    after_discount + gst
)


# =========================================================
# BOOK NOW
# =========================================================

st.write("")

if st.button(
    "🎬 CONFIRM MOVIE BOOKING",
    use_container_width=True
):

    if not customer_name:

        st.warning(
            "⚠️ Please enter your name."
        )

    elif len(selected_seats) != tickets:

        st.warning(
            f"⚠️ Please select exactly {tickets} seat(s)."
        )

    else:

        with st.spinner(
            "🎬 Booking your cinematic experience..."
        ):

            time.sleep(2)


        st.balloons()


        # =================================================
        # BOOKING TICKET
        # =================================================

        st.markdown(
            '<div class="ticket">',
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="ticket-title">'
            '🎫 PRASÉ CINEMA'
            '</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            """
            <p style="
                text-align:center;
                color:#999;
            ">
            OFFICIAL MOVIE TICKET
            </p>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="red-line"></div>',
            unsafe_allow_html=True
        )


        # -------------------------------------------------
        # BOOKING INFORMATION
        # -------------------------------------------------

        st.write(
            f"👤 **Name:** {customer_name}"
        )

        if phone:

            st.write(
                f"📱 **Mobile:** {phone}"
            )


        st.write(
            f"🎬 **Movie:** {selected_movie}"
        )

        st.write(
            f"📅 **Date:** {show_date}"
        )

        st.write(
            f"🕐 **Showtime:** {show_time}"
        )

        st.write(
            f"💺 **Category:** {ticket_type}"
        )

        st.write(
            f"🎟️ **Tickets:** {tickets}"
        )

        st.write(
            f"💺 **Seats:** "
            f"{', '.join(selected_seats)}"
        )


        st.markdown(
            '<div class="red-line"></div>',
            unsafe_allow_html=True
        )


        # -------------------------------------------------
        # PRICE DETAILS
        # -------------------------------------------------

        st.markdown("### 💰 PAYMENT DETAILS")


        st.write(
            f"🎟️ Ticket Price: ₹{ticket_total:.2f}"
        )

        st.write(
            f"🍿 Snacks: ₹{snack_total:.2f}"
        )

        st.write(
            f"🎁 Discount: - ₹{discount:.2f}"
        )

        st.write(
            f"🧾 GST (18%): ₹{gst:.2f}"
        )


        st.write("")


        # -------------------------------------------------
        # GRAND TOTAL
        # -------------------------------------------------

        st.markdown(
            f"""
            <div class="total-box">

                TOTAL PAID

                <br>

                ₹{grand_total:.2f}

            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="red-line"></div>',
            unsafe_allow_html=True
        )


        st.success(
            "🎉 Booking Confirmed! Enjoy your movie!"
        )


        booking_id = (
            "PRASE-"
            +
            datetime.now().strftime("%H%M%S")
        )


        st.info(
            f"🎫 Booking ID: **{booking_id}**"
        )


        st.markdown(
            """
            <p style="
                text-align:center;
                color:#aaa;
                font-size:14px;
            ">
            🍿 Grab your popcorn • 🎬 Enjoy the show • ❤️ Make memories
            </p>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        PRASÉ CINEMA © 2026

        <br><br>

        MOVIES • MEMORIES • MAGIC

    </div>
    """,
    unsafe_allow_html=True
)