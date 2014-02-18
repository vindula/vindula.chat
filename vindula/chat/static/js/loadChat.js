//$j = jQuery.noConflict();
$j(document).ready(function(){
    // load Jappix Mini

    MINI_GROUPCHATS = [];
    MINI_PASSWORDS = [];

    /* Add an animation*/
    MINI_ANIMATE = true;
    MINI_NICKNAME = $j.cookies.get("__nickname");
    
    var username = $j.cookies.get("__ijab_name");
    var password = $j.cookies.get("__ijab_password");

    // launchMini(true, false, $j.cookies.get("__hostname"), username, password);
    
    // Logout ao click no sair 
    $j('#personaltools-logout a').click(function(){
        disconnectMini();           
    });
    
    var width = $j('#jappix_mini').width() + 20;
    $j('#jappix_mini_link').attr('style','right:'+width+'px');
    
    $j('body').mousemove(function(event) {
        var width_now = $j('#jappix_mini').width() + 20;
        if (width != width_now){
            $j('#jappix_mini_link').attr('style','right:'+width_now+'px');
            width = width_now;        
       }
    });
    
    // Exemplo dialog
    $j('a.jm_popup').prepOverlay({
        subtype: 'ajax',
        filter: '#content-core=*,dl.portalMessage.error,dl.portalMessage.info',
        width: '25%',
        config: {fixed:false,speed:'fast',mask:{color:'#000',opacity: 0.4,loadSpeed:0,closeSpeed:0}}
        });
    
    
});