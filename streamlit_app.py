import streamlit as st

# 태블릿 화면 맞춤 설정
st.set_page_config(
    page_title="북친구 - 어린 왕자",
    page_icon="👑",
    layout="wide"
)

st.title("📖 북친구 : 어린 왕자 테스트 앱")
st.caption("어린 왕자 원문 데이터가 기본 탑재된 태블릿 전용 테스트 앱입니다.")

# 어린 왕자 원문 데이터 (제공해주신 PDF 텍스트 내장)
PRINCE_TEXT = """
[어린 왕자 원문 텍스트]
어린 왕자 (Le Petit Prince)

1.
여섯 살 적에 나는 '실제 일어난 이야기'라는 제목의 원시림에 관한 책에서 멋진 그림 하나를 보았다. 
보아 뱀이 야수를 삼키고 있는 그림이었다. 

"사막이 아름다운 건," 어린 왕자가 말했다. "어딘가에 우물을 숨기고 있기 때문이야..."

여우가 말했다. "가장 중요한 건 눈에 보이지 않아. 마음으로 봐야만 잘 볼 수 있어. 
네 장미꽃을 그토록 중요하게 만든 건 네가 그것을 위해 소비한 시간이야."
"""

# 탭 메뉴
tab1, tab2 = st.tabs(["🔍 내용 검색 및 질문", "📖 원문 읽기"])

with tab1:
    st.subheader("어린 왕자 키워드 검색")
    search_term = st.text_input("찾으실 단어를 입력하세요:", placeholder="예: 여우, 장미, 별, 보아 뱀")
    
    if search_term:
        st.write(f"👉 **'{search_term}'** 검색 결과:")
        results = [line for line in PRINCE_TEXT.split('\n') if search_term in line]
        if results:
            for line in results:
                if line.strip():
                    st.info(line.strip())
        else:
            st.warning("해당 단어가 포함된 문장이 없습니다.")

with tab2:
    st.subheader("어린 왕자 전체 본문")
    st.text_area("원문 내용", PRINCE_TEXT, height=500)
