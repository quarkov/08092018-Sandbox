from core.setting import Setting

st = Setting()
n = st.get_setting_ip()
print(n.get_port(), n.get_ip())
