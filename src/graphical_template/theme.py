import matplotlib.font_manager as fm
import matplotlib as mpl
import seaborn as sns

sns.set_theme(context="notebook", style="ticks", palette="deep")

BRAND_COLORS = {
    "Or": "#F36F21",   # orange
    "Rd": "#E41E26", # red
    "l_bl": "#00A7E9",  # light blue
    "d_bl": "#18396A" # dark blue
}

font_path = "src\\graphical_template\\OpenSans-SemiBold.ttf"
font_prop = fm.FontProperties(fname=font_path)
font_name = font_prop.get_name()
fm.fontManager.addfont(font_path)
mpl.rcParams['font.family'] = font_name