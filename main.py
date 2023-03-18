from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock

KV = """
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import Gradient kivy_gradient.Gradient
WindowManager: 
    SplashScreen:
    LoginScreen:
        name:"login"
    SignupScreen:     
    HomePageScreen:  
    SearchScreen:
    ProfileScreen:
    LogoutScreen:

#########################LoginScreen#######################################

<LoginScreen>:
    name: 'login'
    MDLabel:
        text:"Instagram" 
        color:0,0,0,1  
        pos_hint: {'center_x':0.65,'center_y':0.9}
        font_size:50  
        font_name:"D:\ROHIT\kivy app\Poppins-Font-2\Poppins-SemiBold.ttf" 
    MDTextField:
        hint_text: "Phone number,username or email" 
        mode: "rectangle"
        pos_hint: {'center_x':0.54,'center_y':0.7}
        color_mode: 'custom'  
        line_color_focus: 0, 0, 0, 1
        size_hint: None, None
        size: 280, 100
    MDTextField:
        hint_text: "Password"
        mode: "rectangle"
        icon_right:"eye-off"
        pos_hint: {'center_x':0.54,'center_y':0.6}
        color_mode: 'custom'  
        line_color_focus: 0, 0, 0, 1 
        size_hint: None, None
        size: 280, 100 
        password:True
    
    MDRectangleFlatButton:
        text: "Forgotten your password?"
        line_color: 0, 0, 0, 0
        custom_color: "white"
        pos_hint: {'center_x':0.7,'center_y':0.52}
        on_release:
            import webbrowser
            webbrowser.open('https://www.instagram.com/accounts/password/reset/')       
    MDFillRoundFlatButton:
        text: "Log in"
        custom_color: "white"
        pos_hint: {'center_x':0.54,'center_y':0.45}
        size_hint: 0.8, 0.05
        on_press:root.manager.current = 'homepage'
    MDLabel:
        text: "--------------------------------OR--------------------------------"
        pos_hint: {'center_x':0.65,'center_y':0.39}
    MDRectangleFlatIconButton:
        text: "Log in with Facebook"
        icon: "facebook"
        line_color: 0, 0, 0, 0
        custom_color: "white"
        pos_hint: {'center_x':0.54,'center_y':0.35}
        on_release:
            import webbrowser
            webbrowser.open('http://www.facebook.com')
    
    MDLabel:
        text: "Don't have an account?" 
        pos_hint: {'center_x':0.72,'center_y':0.28}  
    MDRectangleFlatButton:
        text: "Sign up"
        line_color: 0, 0, 0, 0
        custom_color: "white"
        pos_hint: {'center_x':0.76,'center_y':0.28}
        on_press:root.manager.current = 'signuppage' 
    MDLabel:
        text: "From"
        color: 0/255, 10/255, 0/255,1
        pos_hint: {'center_x':0.94,'center_y':0.1}                
    MDRectangleFlatIconButton:
        text: "Sign up"
        icon: "infinity"
        line_color: 0, 0, 0, 0
        pos_hint: {'center_x':0.5,'center_y':0.07}

#########################SignupScreen#######################################

<SignupScreen>:
    name: 'signuppage'
    MDLabel:
        text:"Instagram"  
        color:(0/255, 0/255, 0/255,1)   
        pos_hint: {'center_x':0.80,'center_y':0.9}
        font_size:50  
        font_name:"AlexBrush-Regular.ttf"
    MDLabel:
        text:
            '''
            Sign up to see photos and videos 
            ******from your friends.*******'''   
        color:(140/255, 140/255, 140/255,1)   
        pos_hint: {'center_x':0.59,'center_y':0.8}
        font_size:18  
        font_name:"D:\ROHIT\kivy app\Poppins-Font-2\Poppins-Medium.ttf" 
    
    MDFillRoundFlatIconButton:
        text: "Log in with Facebook"
        icon: "facebook"
        line_color: 0, 0, 0, 0
        custom_color: "white"
        size_hint: 0.8, 0.05
        pos_hint: {'center_x':0.54,'center_y':0.69}
        on_release:
            import webbrowser
            webbrowser.open('http://www.facebook.com')            
    MDLabel:
        text: "--------------------------------OR--------------------------------"
        pos_hint: {'center_x':0.65,'center_y':0.62}
    MDTextField:
        hint_text: "Mobile number or email address"
        mode: "rectangle"
        pos_hint: {'center_x':0.52,'center_y':0.54}
        color_mode: 'custom'  
        line_color_focus: 0, 0, 0, 1
        font_size:'10sp'
        size_hint: None, None
        size: 280, 100
    MDTextField:
        hint_text: "Full Name"
        mode: "rectangle"
        pos_hint: {'center_x':0.52,'center_y':0.46}
        color_mode: 'custom'  
        line_color_focus: 0, 0, 0, 1
        font_size:'10sp'
        size_hint: None, None
        size: 280, 100
    MDTextField:
        hint_text: "Username"
        mode: "rectangle"
        pos_hint: {'center_x':0.52,'center_y':0.38}
        color_mode: 'custom'  
        line_color_focus: 0, 0, 0, 1
        font_size:'10sp'
        size_hint: None, None
        size: 280, 100
    MDTextField:
        hint_text: "Password"
        mode: "rectangle"
        pos_hint: {'center_x':0.52,'center_y':0.30}
        color_mode: 'custom'  
        line_color_focus: 0, 0, 0, 1
        font_size:'10sp'
        size_hint: None, None
        size: 280, 100  
    MDFillRoundFlatButton:
        text: "Sign Up"
        line_color: 0, 0, 0, 0
        size_hint: 0.8, 0.05
        pos_hint: {'center_x':0.53,'center_y':0.20}
        on_press: root.manager.current = 'login'

    MDLabel:
        text: 
            '''People who use our service may have uploaded 
            your contact information to Instagram.'''
        font_size:'14sp'
        pos_hint: {'center_x':0.60,'center_y':0.13}  
    MDRectangleFlatButton:
        text: "Learn more"
        line_color: 0, 0, 0, 0
        custom_color: "white"
        pos_hint: {'center_x':0.88,'center_y':0.119}
        on_release:
            import webbrowser
            webbrowser.open('https://www.facebook.com/help/instagram/261704639352628')                                      

    MDLabel:
        text:"By signing up, you agree to our "
        font_size:'14sp'
        pos_hint: {'center_x':0.68,'center_y':0.08} 
    MDRectangleFlatButton:
        text: "Terms,"
        line_color: 0, 0, 0, 0
        custom_color: "white"
        pos_hint: {'center_x':0.78,'center_y':0.08}
        on_release:
            import webbrowser
            webbrowser.open('https://help.instagram.com/581066165581870/?locale=en_GB')
    MDRectangleFlatButton:
        text: "Privacy Policy"
        line_color: 0, 0, 0, 0
        custom_color: "white"
        pos_hint: {'center_x':0.36,'center_y':0.052}
        on_release:
            import webbrowser
            webbrowser.open('https://www.instagram.com/linkshim/?u=https%3A%2F%2Fwww.facebook.com%2Fprivacy%2Fpolicy&e=AT38YmCLwiW25IK9OTJm2bvks_IjVech-gbD9RP0CnZ6_I9A3v-Lf_SSFv_tjghyw8kwbpJVJ93SOccvq5ONuAKFfBQg6YdxgMCwrsJpNznbiRFGchxukMr9nDF_zh8XaSOIOWdQZSDx7e4XlovNuQ')         
    MDRectangleFlatButton:
        text: "and Cookies Policy."
        line_color: 0, 0, 0, 0
        custom_color: "white"
        pos_hint: {'center_x':0.66,'center_y':0.052}
        on_release:
            import webbrowser
            webbrowser.open('https://help.instagram.com/1896641480634370/')

#########################HomePageScreen#######################################

<HomePageScreen>:
    name: 'homepage'
    MDLabel:
        text:"Instagram"  
        color:(0/255, 0/255, 0/255,1)   
        pos_hint: {'center_x':0.58,'center_y':0.95}
        font_size:40  
        font_name:"AlexBrush-Regular.ttf"
        canvas:
            Color:
                rgba: 230/255, 230/255, 230/255, 1    
            Rectangle:
                pos: 0.5,0.5
                size: 400,60
            Color:
                rgba: 211/255, 211/255, 211/255, 1    
            Ellipse:
                pos:10,510
                size:75,75
                source:'av.png'      
            Ellipse:
                pos:100,510
                size:75,75 
                source:'f1.png' 
            Ellipse:
                pos:190,510
                size:75,75
                source:'f2.png'   
            Ellipse:
                pos:280,510
                size:75,75        
                source:'f3.png'  
            Ellipse:
                pos:50,65
                size:25,25        
                source:'f3.png'
            Ellipse:
                pos:65,65
                size:25,25        
                source:'av.png'   
            Ellipse:
                pos:80,65
                size:25,25        
                source:'f2.png'          
    MDLabel:
        text: "Liked by rohan and 100 others"
        color:0,0,0,1
        pos_hint: {'center_x': 0.8,'center_y': 0.12}
    MDIconButton:
        icon: "plus"   
        icon_size: "35sp"
        pos_hint: {"center_x": .19, "center_y": .81}            
    MDIconButton:
        icon: "plus-box"
        icon_size: "35sp"
        pos_hint: {"center_x": .79, "center_y": .95}
    MDIconButton:
        icon: "facebook-messenger"
        icon_size: "35sp"
        pos_hint: {"center_x": .92, "center_y": .95}
    MDIconButton:
        icon: "home"
        icon_size: "35sp"
        pos_hint: {"center_x": .15, "center_y": .05}
    MDIconButton:
        icon: "magnify"
        icon_size: "35sp"
        pos_hint: {"center_x": .32, "center_y": .05}   
        on_press: root.manager.current = 'search' 
    MDIconButton:
        icon: "movie"
        icon_size: "35sp"
        pos_hint: {"center_x": .52, "center_y": .05}
    MDIconButton:
        icon: "heart-outline"
        icon_size: "35sp"
        pos_hint: {"center_x": .72, "center_y": .05}
    MDCard:
        size_hint: None, None
        size: "40dp", "40dp"        
        border_radius: 20
        radius: [15]    
        pos_hint: {"center_x": .90, "center_y": .05}
        on_press: root.manager.current = 'profile'
        Image:
            source:'av2.png'
            
    MDCard:
        size_hint: None, None
        size: "350dp", "300dp"
        pos_hint: {"center_x": .50, "center_y": .43}
        md_bg_color:255/255, 255/255, 255/255, 1
        Image:
            source:"rohit.jpeg"
 
    TwoLineAvatarListItem:
        text: "rohitkumar"
        secondary_text: "Jecrc University" 
        pos_hint: {'center_x': 0.55,'center_y': 0.72}   
        ImageLeftWidget:
            source: "av.png" 
    MDIconButton:
        icon: "heart-outline"
        icon_size: "30sp"
        pos_hint: {"center_x": .19, "center_y": .175} 

    MDIconButton:
        icon: "chat-outline"
        icon_size: "30sp"
        pos_hint: {"center_x": .32, "center_y": .175}
    MDIconButton:
        icon: "share-outline"
        icon_size: "30sp"
        pos_hint: {"center_x": .44, "center_y": .175}          
    MDIconButton:
        icon: "bookmark-outline"
        icon_size: "30sp"
        pos_hint: {"center_x": .85, "center_y": .175} 
    MDIconButton:
        icon: "dots-vertical"
        icon_size: "35sp"
        pos_hint: {"center_x": .85, "center_y": .72}

########################SearchScreen#######################################
<SearchScreen>:
    name:'search'
    MDTextField:
        hint_text: "Search"
        mode: "rectangle"
        icon_left:"magnify"
        pos_hint: {'center_x':0.5,'center_y':0.96}
        color_mode: 'custom'  
        line_color_focus: 0, 0, 0, 1 
        size_hint: None, None
        size: 340, 30
    MDIconButton:
        icon: "home"
        icon_size: "35sp"
        pos_hint: {"center_x": .15, "center_y": .05}
        on_press: root.manager.current = 'homepage'
    GridLayout:
        rows:4
        cols:3
        pos_hint: {'center_x':0.6,'center_y':0.3}
       
        Image:
            source: "rohit.jpeg"
            size_hint: None, None
            size: "100dp", "100dp"    
        Image:
            source: "rohiy.jpeg"
            size_hint: None, None
            size: "100dp", "100dp"    
        Image:
            source: "rohiy.jpeg"
            size_hint: None, None
            size: "100dp", "100dp"
            
        Image:
            source: "rohiy.jpeg"
            size_hint: None, None
            size: "100dp", "100dp" 
        Image:
            source: "rohiy.jpeg"
            size_hint: None, None
            size: "100dp", "100dp" 
        Image:
            source: "rohiy.jpeg"
            size_hint: None, None
            size: "100dp", "100dp"
        Image:
            source: "rohiy.jpeg"
            size_hint: None, None
            size: "100dp", "100dp"
        Image:
            source: "rohiy.jpeg"
            size_hint: None, None
            size: "100dp", "100dp"
        Image:
            source: "rohiy.jpeg"
            size_hint: None, None
            size: "100dp", "100dp"        
























########################ProfileScreen#######################################

<ProfileScreen>:
    name:'profile'
    MDLabel:
        text:"rohitkumar"
        font_size:'30sp'
        pos_hint: {'center_x':0.6,'center_y':0.97}
        canvas:
            Color:
                rgba: 211/255, 211/255, 211/255, 1    
            Ellipse:
                pos:10,510
                size:75,75
                source:'av.png'
    MDLabel:
        text:"Bio"
        pos_hint: {'center_x':0.6,'center_y':0.75}     
    MDLabel:
        text:
            '''100            1M              1M
            Posts   Followers    Following''' 
        pos_hint: {'center_x':0.85,'center_y':0.85} 
    MDRaisedButton:
        text: "Edit Profile"
        text_color:0,0,0,1
        md_bg_color: 184/255,184/255,184/255,1
        pos_hint: {'center_x':0.23,'center_y':0.65}
        size_hint: 0.4, 0.06
    MDRaisedButton:
        text: "Share Profile"
        text_color:0,0,0,1
        md_bg_color: 184/255,184/255,184/255,1
        pos_hint: {'center_x':0.65,'center_y':0.65}
        size_hint: 0.4, 0.06
    MDIconButton:
        icon: "account-plus"
        icon_size: "32sp"
        pos_hint: {'center_x':0.92,'center_y':0.65}

    MDIconButton:
        icon: "lock"   
        icon_size: "30sp"
        pos_hint: {"center_x": .05, "center_y":0.97}            
    MDIconButton:
        icon: "chevron-down"
        icon_size: "30sp"
        pos_hint: {"center_x": .56, "center_y":0.97}
    MDIconButton:
        icon: "plus-box"
        icon_size: "30sp"
        pos_hint: {"center_x": .82, "center_y": 0.97}
    MDIconButton:
        icon: "reorder-horizontal"
        icon_size: "30sp"
        pos_hint: {"center_x": .93, "center_y":0.97}
        on_press: root.manager.current = 'logout'

    MDIconButton:
        icon: "grid"
        icon_size: "30sp"
        pos_hint: {"center_x": .23, "center_y":0.55}
    MDLabel:
        text:"------------------------------------------"
        pos_hint: {"center_x": .55, "center_y": .5}    
    MDIconButton:
        icon: "image-filter-frames"
        icon_size: "30sp"
        pos_hint: {"center_x": .73, "center_y":0.55}        
    Image:
        source: "rohit.jpeg"
        pos_hint: {"center_x": .2, "center_y": .39}
        size_hint: None, None
        size: "120dp", "120dp"    
    Image:
        source: "rohiy.jpeg"
        pos_hint: {"center_x": .5, "center_y": .39}
        size_hint: None, None
        size: "120dp", "120dp"    
    Image:
        source: "rohiy.jpeg"
        pos_hint: {"center_x": .8, "center_y": .39}
        size_hint: None, None
        size: "120dp", "120dp" 
    Image:
        source: "rohiy.jpeg"
        pos_hint: {"center_x": .2, "center_y": .2}
        size_hint: None, None
        size: "120dp", "120dp" 
    Image:
        source: "rohiy.jpeg"
        pos_hint: {"center_x": .5, "center_y": .2}
        size_hint: None, None
        size: "120dp", "120dp" 
    Image:
        source: "rohiy.jpeg"
        pos_hint: {"center_x": .8, "center_y": .2}
        size_hint: None, None
        size: "120dp", "120dp"                            
    MDLabel:
        canvas:
            Color:
                rgba: 230/255, 230/255, 230/255, 1    
            Rectangle:
                pos: 0.5,0.5
                size: 400,60
    MDIconButton:
        icon: "home"
        icon_size: "35sp"
        pos_hint: {"center_x": .15, "center_y": .05}
        on_press: root.manager.current = 'homepage'
    MDIconButton:
        icon: "magnify"
        icon_size: "35sp"
        pos_hint: {"center_x": .32, "center_y": .05}    
    MDIconButton:
        icon: "video-box"
        icon_size: "35sp"
        pos_hint: {"center_x": .52, "center_y": .05}
    MDIconButton:
        icon: "heart-outline"
        icon_size: "35sp"
        pos_hint: {"center_x": .72, "center_y": .05}
    MDIconButton:
        icon: "account"
        icon_size: "35sp"
        pos_hint: {"center_x": .90, "center_y": .05}
    
########################LogoutScreen#######################################

<LogoutScreen>:
    name:"logout"
    MDLabel:
        text:"Settings"
        pos_hint: {"center_x": .4, "center_y": .94}
        halign:"center"
        theme_text_color:"Custom"
        text_color:0,0,0,1
        font_size:"35sp"
        font_name:"D:\\ROHIT\\kivy app\\Poppins-Font-2\\Poppins-Regular.ttf"
    MDIconButton:
        icon: "arrow-left"
        icon_size: "35sp"
        pos_hint: {"center_x": .12, "center_y": .94}
        on_press: root.manager.current = 'profile'    
    MDTextField:
        hint_text: "Search"
        mode: "rectangle"
        icon_left:"magnify"
        pos_hint: {'center_x':0.5,'center_y':0.85}
        color_mode: 'custom'  
        line_color_focus: 0, 0, 0, 1 
        size_hint: None, None
        size: 300, 30
    MDRectangleFlatIconButton:    
        text: "Follow and invite friends"
        font_size:'20sp'
        icon:"account-plus"
        line_color: 0, 0, 0, 0
        pos_hint: {'center_x':0.4,'center_y':0.75}
    MDRectangleFlatIconButton:    
        text: "Notifications"
        font_size:'20sp'
        icon:"bell"
        line_color: 0, 0, 0, 0
        pos_hint: {'center_x':0.26,'center_y':0.7}

    MDRectangleFlatIconButton:    
        text: "Privacy"
        font_size:'20sp'
        icon:"lock"
        line_color: 0, 0, 0, 0
        pos_hint: {'center_x':0.19,'center_y':0.65}
    MDRectangleFlatIconButton:    
        text: "Supervision"
        font_size:'20sp'
        icon:"account-multiple"
        line_color: 0, 0, 0, 0
        pos_hint: {'center_x':0.25,'center_y':0.60}
    MDRectangleFlatIconButton:    
        text: "Security"
        font_size:'20sp'
        icon:"security"
        line_color: 0, 0, 0, 0
        pos_hint: {'center_x':0.20,'center_y':0.55}
    MDRectangleFlatIconButton:    
        text: "Ads"
        font_size:'20sp'
        icon:"bullhorn"
        line_color: 0, 0, 0, 0
        pos_hint: {'center_x':0.15,'center_y':0.50}
    MDRectangleFlatIconButton:    
        text: "Account"
        font_size:'20sp'
        icon:"account-circle-outline"
        line_color: 0, 0, 0, 0
        pos_hint: {'center_x':0.20,'center_y':0.45}
    MDRectangleFlatIconButton:    
        text: "Help"
        font_size:'20sp'
        icon:"help-box"
        line_color: 0, 0, 0, 0
        pos_hint: {'center_x':0.16,'center_y':0.40}
    MDRectangleFlatIconButton:    
        text: "About"
        font_size:'20sp'
        icon:"alert-circle-outline"
        line_color: 0, 0, 0, 0
        pos_hint: {'center_x':0.17,'center_y':0.35}

    MDRectangleFlatIconButton:    
        text: "Theme"
        font_size:'20sp'
        icon:"puzzle-heart-outline"
        line_color: 0, 0, 0, 0
        pos_hint: {'center_x':0.19,'center_y':0.30}
    MDLabel:
        text:"Logins"
        font_size:'30sp'
        pos_hint: {'center_x':0.55,'center_y':0.22}
    MDRectangleFlatButton:
        text: "Add account"
        text_color:0,0,0,1
        pos_hint: {'center_x':0.23,'center_y':0.15}
        size_hint: 0.4, 0.06    
    MDRectangleFlatButton:
        text: "Logout"
        text_color:0,0,0,1
        pos_hint: {'center_x':0.23,'center_y':0.07}
        size_hint: 0.4, 0.06 
        on_press: root.manager.current = 'login'                
    

########################SplashScreen#######################################

<SplashScreen>:  
    RelativeLayout:
        FloatLayout
            canvas:
                Rectangle:
                    size: self.size
                    pos: self.pos
                    texture: Gradient.vertical(get_color_from_hex("#ff5050"), get_color_from_hex("#990099"))
            Image:
                source:"in.png"
                pos_hint: {"center_x": .53, "center_y": .75}
                size_hint: 0.40, 0.40
            MDLabel:
                text:"Instagram"
                pos_hint: {"center_x": .5, "center_y": .35}
                halign:"center"
                theme_text_color:"Custom"
                text_color:1,1,1,1
                font_size:"35sp"
                font_name:"D:\\ROHIT\\kivy app\\Poppins-Font-2\\Poppins-Bold.ttf" 
            
            MDLabel:
                text:"By Rohit"
                pos_hint: {"center_x": .49, "center_y": .2}
                halign:"center"
                theme_text_color:"Custom"
                text_color:1,1,1,1
                font_size:"18sp"
                font_name:"D:\\ROHIT\\kivy app\\Poppins-Font-2\\Poppins-Medium.ttf"  
          

"""         


class InstaApp(MDApp):
    
    def build(self):
        global screen
        screen=Screen()
        Window.size = (360,650)
        self.window_manager=Builder.load_string(KV)
        Clock.schedule_once(self.go_to_login,5)
        return self.window_manager

    class WindowManager(ScreenManager):
        pass 

    class LoginScreen(Screen):
        pass 
    class ProfileScreen(Screen):
        pass   
    class SplashScreen(Screen):
        pass 
    class HomePageScreen(Screen):
        pass
    class SignupScreen(Screen):
        pass
    class LogoutScreen(Screen):
        pass
    class SearchScreen(Screen):
        pass

    def go_to_login(self,*args):
        self.window_manager.current='login'
        return screen   
if __name__=="__main__":
    InstaApp().run()