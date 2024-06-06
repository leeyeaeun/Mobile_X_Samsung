import i18n
import streamlit as st

from utils.init import init_once


if __name__ == '__main__':
    # Init
    init_once()

    st.image("https://i.namu.wiki/i/VWbFu3I6Ifbry54TQw0YegJPHCtvEkNjTAmNBwu5whguc6ueUBUYes6yA3mrWqBgvTf8YHJFBzUX1qvoN3aJelnPQJKRW8INKyF8ZhGzpgYz43L9koeuRPvxe9n2xD5JPr5BpelftvWwbBc37_R4IA.svg"
    ,width=300)

    # Show title
    st.title(i18n.t('common.title'))

    # Show page description
    st.write(i18n.t('common.description'))

    # Show github link
    st.write(f"* Github: {i18n.t('common.github')}")
