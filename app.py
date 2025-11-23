import streamlit as st
import pandas as pd
import requests

# --- 設定頁面配置 ---
st.set_page_config(
    page_title="東京六日奧德賽 v2.0",
    page_icon="🗼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 🛠️ 功能函數區 (後端邏輯) ---

# 1. 取得東京即時天氣 (使用 Open-Meteo 免費 API)
def get_tokyo_weather():
    try:
        # 東京座標: 緯度 35.6895, 經度 139.6917
        url = "https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&current=temperature_2m,weather_code&timezone=Asia%2FTokyo"
        response = requests.get(url)
        data = response.json()
        
        temp = data['current']['temperature_2m']
        w_code = data['current']['weather_code']
        
        # 簡單的天氣代碼轉換
        if w_code <= 3: weather_icon = "☀️ 晴朗/多雲"
        elif w_code <= 48: weather_icon = "🌫️ 起霧"
        elif w_code <= 67: weather_icon = "🌧️ 下雨"
        elif w_code <= 77: weather_icon = "❄️ 下雪"
        else: weather_icon = "🌦️ 陣雨"
        
        return f"{weather_icon} {temp}°C"
    except:
        return "無法取得天氣"

# 2. 產生 Google Maps 導航按鈕
def map_btn(location_name, label="📍 導航去這裡"):
    # 將地點名稱編碼為 URL 格式
    base_url = "https://www.google.com/maps/search/?api=1&query="
    map_url = base_url + location_name
    st.link_button(label, map_url, help=f"開啟 Google Maps 導航至 {location_name}")

# --- 側邊欄：天氣與導航 ---
st.sidebar.title("🗼 東京深度遊導航")

# 顯示即時天氣
current_weather = get_tokyo_weather()
st.sidebar.metric(label="東京目前天氣", value=current_weather)

st.sidebar.markdown("### 📅 日期：12/19 - 12/24")

menu = ["🏠 總覽與行前準備", "Day 1: 抵達與東京心臟", "Day 2: 鎌倉古都風情", 
        "Day 3: 下町文化漫步", "Day 4: 動漫與吉卜力", "Day 5: 迪士尼與晴空塔", "Day 6: 購物與返程"]
choice = st.sidebar.radio("前往行程", menu)

st.sidebar.markdown("---")
st.sidebar.info("**緊急聯絡**\n\n📞 旅外國人急難救助：\n+81-3-3280-7917")

# --- 頁面內容邏輯 ---

if choice == "🏠 總覽與行前準備":
    st.title("🗼 東京六天五夜深度遊：總覽")
    st.markdown("### 📝 您的專屬行程報告書")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### ⚠️ 關鍵任務")
        st.checkbox("11/10 前：搶訂「三鷹之森吉卜力美術館」門票")
        st.checkbox("提前預訂：東京迪士尼海洋門票")
        st.checkbox("下載 Suica/PASMO 到 Apple Pay/Google Pay")
        
    with col2:
        st.markdown("#### 🏨 住宿建議區域")
        st.write("建議住在 **東京車站** 或 **上野站** 附近，方便搭乘新幹線與機場快線。")
        map_btn("東京車站飯店", "🏨 搜尋東京車站附近飯店")

elif choice == "Day 1: 抵達與東京心臟":
    st.header("Day 1 (12/19 週五): 抵達與東京心臟")
    
    st.info("✈️ **16:00** 抵達成田機場 (NRT)")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("#### 1. 前往東京市區")
        st.write("搭乘 **N'EX 成田特快** 直達東京站 (約 53 分鐘)。")
    with col2:
        map_btn("成田機場第2航廈站", "🚆 導航至 N'EX 月台")

    st.markdown("---")
    st.markdown("#### 2. 晚間：東京車站一番街")
    st.write("位於東京車站八重洲地下中央口，無需出站即可抵達。")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("https://lh3.googleusercontent.com/p/AF1QipNq4w2_X5Q4w2_X5Q4w2_X5Q4w2_X5Q4w2_X5Q4w=s680-w680-h510", use_column_width=True)
        st.markdown("**東京拉麵街**")
        map_btn("東京拉麵街", "🍜 導航至拉麵街")
    with c2:
        st.markdown("**動漫人物街**")
        st.caption("Jump Shop, Pokémon Store")
        map_btn("東京動漫人物街", "🧸 導航至動漫街")
    with c3:
        st.markdown("**東京零食樂園**")
        st.caption("現炸 Calbee 薯條")
        map_btn("東京零食樂園", "🍟 導航至零食樂園")

elif choice == "Day 2: 鎌倉古都風情":
    st.header("Day 2 (12/20 週六): 鎌倉古都風情")
    
    st.markdown("### 上午：鶴岡八幡宮與小町通")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("從鎌倉站東口出來，穿過熱鬧的小町通商店街，盡頭即是八幡宮。")
    with col2:
        map_btn("鶴岡八幡宮", "⛩️ 導航：八幡宮")

    st.markdown("### 下午：長谷寺與大佛")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("搭乘江之電至「長谷站」。參觀著名的觀音像與露天大佛。")
    with col2:
        map_btn("高德院 鎌倉大佛", "🧘 導航：鎌倉大佛")

    st.markdown("### 黃昏：灌籃高手平交道")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Enoden_Kamakurakokomae_Station_crossing_20181223.jpg/640px-Enoden_Kamakurakokomae_Station_crossing_20181223.jpg")
    map_btn("鎌倉高校前駅", "🏀 導航：灌籃高手平交道")

elif choice == "Day 3: 下町文化漫步":
    st.header("Day 3 (12/21 週日): 上野與谷中銀座")
    
    st.subheader("📍 上野恩賜公園")
    st.write("包含上野東照宮、動物園、美術館的廣大園區。")
    map_btn("上野恩賜公園", "🌲 導航至上野公園")
    
    st.markdown("---")
    st.subheader("📍 谷中銀座商店街")
    st.write("從日暮里站西口步行，經過「夕陽階梯」抵達。感受昭和時期的懷舊氛圍。")
    map_btn("谷中銀座商店街", "🐈 導航至谷中銀座")
    
    st.info("💡 推薦：在商店街購買「鈴木肉店」的炸肉餅邊走邊吃。")

elif choice == "Day 4: 動漫與吉卜力":
    st.header("Day 4 (12/22 週一): 吉卜力與吉祥寺")
    
    st.error("🎟️ **請確認已攜帶吉卜力門票與護照！**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 三鷹之森吉卜力美術館")
        st.write("位於三鷹站南口，可搭乘黃色接駁巴士或沿著「風之散步道」步行。")
        map_btn("三鷹之森吉卜力美術館", "🤖 導航至美術館")
    
    with col2:
        st.markdown("### 吉祥寺 (Kichijoji)")
        st.write("穿過井之頭公園即可抵達吉祥寺商圈。")
        map_btn("吉祥寺", "🛍️ 導航至吉祥寺站")

elif choice == "Day 5: 迪士尼與晴空塔":
    st.header("Day 5 (12/23 週二): 迪士尼海洋 & 晴空塔")
    
    st.markdown("### 🌊 東京迪士尼海洋 (DisneySea)")
    st.write("搭乘 JR 京葉線至舞濱站，轉乘迪士尼單軌電車。")
    map_btn("東京迪士尼海洋", "🌋 導航至迪士尼海洋入口")
    
    st.markdown("---")
    st.markdown("### 🗼 東京晴空塔 (Skytree)")
    st.write("晚上前往押上站，欣賞東京夜景。")
    map_btn("東京晴空塔", "🌃 導航至晴空塔")

elif choice == "Day 6: 購物與返程":
    st.header("Day 6 (12/24 週三): 酒々井 Outlets")
    
    st.warning("⏰ 航班時間：14:00 (請務必於 12:00 前抵達機場)")
    
    st.markdown("### 🛍️ 酒々井 Premium Outlets")
    st.write("距離成田機場最近的 Outlet，有直達巴士往返機場 (約 15 分鐘)。")
    
    c1, c2 = st.columns(2)
    with c1:
        st.write("**步驟 1：東京前往 Outlet**")
        st.caption("東京站八重洲口搭乘巴士")
        map_btn("酒々井 Premium Outlets", "🚌 導航至 Outlets")
    
    with c2:
        st.write("**步驟 2：Outlet 前往機場**")
        st.caption("搭乘 11:30 或 12:00 的接駁巴士")
        map_btn("成田國際機場", "✈️ 導航至成田機場")

# --- 頁尾 ---
st.markdown("---")
st.caption("Designed by Gemini Expert Travel Partner | v2.0 with Live Weather & Maps")
