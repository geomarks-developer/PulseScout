"""PulseScout home screen."""
from __future__ import annotations

import streamlit as st
from app_utils import initialize_settings

from securities import get_security_options, format_security_option

initialize_settings()
st.set_page_config(
    page_title="PulseScout",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Hide the sidebar expand arrow/control
st.markdown(
    """
    <style>
    [data-testid="collapsedControl"] {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
<style>
[data-testid="stSidebar"] {display: none;}
[data-testid="collapsedControl"] {display: none;}
.block-container {
    max-width: 520px;
    padding-top: 2.75rem;
    padding-left: 1rem;
    padding-right: 1rem;
    padding-bottom: 5rem;
}
.ms-brand {
    font-size: 2rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: .2rem;
}
.ms-subtitle {
    color: #9aa3b2;
    font-size: .95rem;
    margin-bottom: 1.25rem;
}
.ms-card {
    border: 1px solid rgba(128,128,128,.25);
    background: rgba(128,128,128,.055);
    border-radius: 18px;
    padding: 1rem 1rem .8rem 1rem;
    margin-bottom: .65rem;
}
.ms-card-title {
    font-size: 1.18rem;
    font-weight: 750;
    margin-bottom: .2rem;
}
.ms-card-text {
    color: #9aa3b2;
    font-size: .88rem;
    line-height: 1.4;
}
.quick-label {
    font-size: .9rem;
    color: #9aa3b2;
    margin-top: .8rem;
    margin-bottom: .25rem;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="ms-brand">📱 PulseScout</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="ms-subtitle">Stocks, ETFs, value, growth, and income research, from a bespoke list of quality tickers, in one mobile-first workspace.</div>',
    unsafe_allow_html=True,
)

selected_security = st.selectbox(
    "Search",
    options=get_security_options(),
    index=None,
    placeholder="Search a ticker, ETF, or company...",
    format_func=format_security_option,
    label_visibility="collapsed",
)

if selected_security:
    st.session_state["mobile_selected_ticker"] = selected_security
    st.switch_page("pages/details.py")

default_pages = {"Growth":"pages/growth.py","Value":"pages/value.py","Dividend":"pages/dividend.py","ETF":"pages/etf.py","Markets":"pages/markets.py"}
default_module = st.session_state.get("mobile_default_module", "Growth")
st.page_link(default_pages.get(default_module, "pages/growth.py"), label=f"Open default: {default_module}", icon="🚀", width="stretch")
st.markdown('<div class="quick-label">RESEARCH</div>', unsafe_allow_html=True)

cards = [
    ("📈", "Growth", "Find businesses with strong expansion, quality, and momentum.", "pages/growth.py"),
    ("💎", "Value", "Find attractive valuations while watching quality and value-trap risk.", "pages/value.py"),
    ("💰", "Dividend", "Research income, dividend quality, sustainability, and safety.", "pages/dividend.py"),
    ("🌐", "ETF", "Explore ETFs, sectors, performance, expenses, and allocation ideas.", "pages/etf.py"),
]

for icon, title, description, page in cards:
    st.markdown(
        f'<div class="ms-card"><div class="ms-card-title">{icon} {title}</div>'
        f'<div class="ms-card-text">{description}</div></div>',
        unsafe_allow_html=True,
    )
    st.page_link(page, label=f"Open {title}", icon=icon, width="stretch")

st.markdown('<div class="quick-label">QUICK ACCESS</div>', unsafe_allow_html=True)
q1, q2 = st.columns(2)
with q1:
    st.page_link("pages/watchlist.py", label="Watchlist", icon="⭐", width="stretch")
    st.page_link("pages/compare.py", label="Compare", icon="⚖️", width="stretch")
with q2:
    st.page_link("pages/markets.py", label="Markets", icon="🌐", width="stretch")
    st.page_link("pages/settings.py", label="Settings", icon="⚙️", width="stretch")
st.page_link("pages/score_guide.py", label="Score Guide", icon="📖", width="stretch")

st.divider()
st.caption("PulseScout • Research tools for informational and educational use")
