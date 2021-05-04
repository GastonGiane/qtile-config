from typing import List
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()
wallpaper_image = '/data/Pictures/Wallpapers/wallhaven-qd66vd.png'
browser = "firefox --new-tab "
private_browser = "firefox --private-window"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod],
        "Tab",
        lazy.layout.next(),
        desc="Move window focus to other window"),
    Key([mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"],
        "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"],
        "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"],
        "j",
        lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"],
        "Return",
        lazy.spawn("emacs"),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "p", lazy.spawn("dmenu_run"), desc="Launch terminal"),
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"],
        "f",
        lazy.window.toggle_floating(),
        desc="Put the focused window to/from floating mode"),
    Key([mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Put the focused window to/from fullscreen mode"),
    Key([mod],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +500"),
        desc="Increase volume"),
    Key([],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -500"),
        desc="Decrease volume"),
    Key([],
        "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
        desc="Mute volume"),
    Key([],
        "XF86AudioMicMute",
        lazy.spawn("pactl set-source-mute @DEFAULT_SOURCE@ toggle"),
        desc="Mute microphone"),
    Key([],
        "XF86AudioPlay",
        lazy.spawn("mocp -G"),
        desc="Toggle between playing and paused"),
    Key([], "XF86AudioStop", lazy.spawn("mocp -s"), desc="Stop playing"),
    Key([], "XF86AudioNext", lazy.spawn("mocp -f"), desc="Play the next song"),
    Key([],
        "XF86AudioPrev",
        lazy.spawn("mocp -r"),
        desc="Play the previous song"),
    Key([mod],
        "s",
        lazy.spawn("school-meetings"),
        desc="Launch school meetings script"),
    KeyChord([mod], "t", [
        Key([], "p", lazy.spawn(terminal + " -e pulsemixer")),
        Key([], "m", lazy.spawn(terminal + " -e mocp")),
    ]),
    KeyChord([mod], "b", [
        Key([], "p", lazy.spawn(private_browser)),
        Key([], "g", lazy.spawn(browser + "https://github.com/GastonGiane")),
        Key([], "t", lazy.spawn(browser + "https://twitter.com/home")),
        Key([], "r", lazy.spawn(browser + "http://rarbggo.org/torrents.php")),
        Key([], "b", lazy.spawn(browser + "https://duckduckgo.com/")),
        Key([], "y", lazy.spawn(browser + "https://youtube.com/")),
        Key([], "m", lazy.spawn(browser + "https://mail.google.com/mail/")),
        Key([], "c",
            lazy.spawn(browser + "https://calendar.google.com/calendar/")),
    ]),
]

mouse = [
    Drag([mod],
         "Button1",
         lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod],
         "Button3",
         lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

groups = [
    Group("1", label="1"),
    Group("2", label="2", matches=[Match(wm_class=["firefox"])]),
    Group("3", label="3"),
    Group("4", label="4"),
    Group("5", label="5"),
    Group("6", label="6"),
    Group("7", label="7"),
    Group("8",
          label="8",
          matches=[Match(wm_class=["Skype", "zoom", "TelegramDesktop"])]),
    Group("9", label="9", matches=[Match(wm_class=["obs"])]),
]

for i in groups:
    keys.extend([
        Key([mod],
            i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),
        Key([mod, "shift"],
            i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

layout_config = {
    "border_normal": "#1d2021",
    "border_focus": "#7daea3",
    "margin": 10,
    "insert_position": 1,
}

layouts = [
    layout.Columns(**layout_config),
    layout.Max(),
]

floating_layout = layout.Floating(**layout_config,
                                  float_rules=[
                                      *layout.Floating.default_float_rules,
                                      Match(wm_class='confirmreset'),
                                      Match(wm_class='makebranch'),
                                      Match(wm_class='maketag'),
                                      Match(wm_class='ssh-askpass'),
                                      Match(wm_class='Skype'),
                                      Match(title='branchdialog'),
                                      Match(title='pinentry'),
                                  ])

widget_defaults = dict(
    font='JetBrains Mono',
    fontsize=12,
    padding=3,
    background='#1d2021',
    foreground='#d4be98',
)

extension_defaults = widget_defaults.copy()

screens = [
    # Main Screen
    Screen(
        wallpaper=wallpaper_image,
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.GroupBox(hide_unused=True,
                                highlight_method='block',
                                disable_drag=True,
                                urgent_alert_method='block'),
                widget.Prompt(),
                widget.CurrentLayoutIcon(scale=0.6),
                widget.WindowName(),
                widget.Moc(),
                widget.Net(format=' {down} ↓ ↑ {up} |'),
                widget.Clock(format='%a %d %b - %H:%M '),
                widget.Systray(),
            ],
            28,
        ),
    ),
    # Second Screen
    Screen(
        wallpaper=wallpaper_image,
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.GroupBox(hide_unused=True,
                                highlight_method='block',
                                disable_drag=True,
                                urgent_alert_method='block'),
                widget.CurrentLayoutIcon(scale=0.6),
                widget.WindowName(),
                widget.Clock(format='%a %d %b - %H:%M '),
            ],
            25,
        ),
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"
