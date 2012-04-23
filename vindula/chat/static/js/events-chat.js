 $j = jQuery.noConflict();
 $j(document).ready(function () {    
    //
    // Presence handler
    //
    $j(document).bind('jarnxmpp.presence', function (event, jid, status, presence) {
        var user_id = Strophe.getNodeFromJid(jid),
            barejid = Strophe.getBareJidFromJid(jid),
            existing_user_element = $j('#online-users-' + user_id),
            online_count;
        if (barejid === Strophe.getBareJidFromJid(jarnxmpp.connection.jid)) {
            return;
        }
        if (existing_user_element.length) {
            if (status == 'offline' && jarnxmpp.Presence.online.hasOwnProperty(user_id)) {
                return;
            }
            if (status == 'offline'){
                existing_user_element.remove();
            }
            existing_user_element.attr('class', status);
        } else {
            $j.get(portal_url + '/xmpp-userDetails?jid=' + barejid, function (user_details) {
                if ($j('#online-users-' + user_id).length > 0) {
                    return;
                }
                user_details = $j(user_details);
                /* Set-up following link.
                jarnxmpp.PubSub.getSubscriptions(function (following) {
                    var $jfollowing = $j('a.followingStatus', user_details);
                    if (following.indexOf('people') !== -1) {
                        $jfollowing.remove();
                        return;
                    }
                    if (following.indexOf(user_id) === -1) {
                        $jfollowing.text(jarnxmpp.UI._('Follow user'));
                    } else {
                        $jfollowing.text(jarnxmpp.UI._('Unfollow user'));
                    }
                });*/
                
                $j('#online-users').append(user_details);
                /*$j('#online-users li[data-userid]').sortElements(function (a, b) {
                    return $j('a.user-details-toggle', a).text().trim() > $j('a.user-details-toggle', b).text().trim() ? 1 : -1;
                });*/
            });
            // Pre-fetch user info if we have a session storage.
            if (jarnxmpp.Storage.storage !== null) {
                jarnxmpp.Presence.getUserInfo(user_id, function (data) {});
            }
        }
        online_count = jarnxmpp.Presence.onlineCount();
        if (online_count > 0) {
            $j('#no-users-online').hide();
        } else {
            $j('#no-users-online').show();
        }
        $j('#online-count').text(online_count);
    });
    
    //
    // Message handler
    //
    $j(document).bind('jarnxmpp.message', function (event) {
        var user_id = Strophe.getNodeFromJid(event.from),
        text = '<div class="chatboxmessage">\
                   <span class="chatboxmessagefrom">'+user_id.toUpperCase()+':&nbsp;&nbsp;</span>\
                   <span class="chatboxmessagecontent">'+event.body+'</span>\
                </div>';            
            
            //$form = $j('#online-users li#online-users-' + user_id + ' .replyForm').clone(),
            //$reply_p = $j('<p>').append($form),
            //text = $j('<span>').append($text_p); //.append($reply_p).remove().html();
        
        createChatBox(user_id, 0 ,text);
        //$j('input[type="submit"]', $form).attr('value', 'Reply');

        jarnxmpp.Presence.getUserInfo(user_id, function (data) {
            /*var gritter_id = $j.gritter.add({
                title: data.fullname,
                text: text,
                image: data.portrait_url,
                sticky: true,
                after_close: function () {
                    if (jarnxmpp.UI.msg_counter > 1) {
                        jarnxmpp.UI.msg_counter -= 1;
                    } else {
                        jarnxmpp.UI.msg_counter = 0;
                    }
                    jarnxmpp.UI.updateMsgCounter();
                }
            });*/
            // Let the form know the gritter id so that we can easily close it later.
            //$j('#gritter-item-' + gritter_id + ' form').attr('data-gritter-id', gritter_id);

            //jarnxmpp.UI.msg_counter += 1;
            //jarnxmpp.UI.updateMsgCounter();
        });
    });
        /*
        // Send message
        //
        $j('.sendXMPPMessage').live('submit', function (e) {
            var $field = $('[name="message"]:input', this),
                text = $field.val(),
                recipient = $field.attr('data-recipient'),
                message;
            $j(this).parents('.user-details-form')
                .parent()
                .children('.user-details-toggle')
                .removeClass('expanded');
            var gritter_id = $(this).attr('data-gritter-id');
            if (typeof (gritter_id) !== 'undefined') {
                $.gritter.remove(gritter_id);
            }
            $j("div#online-users-container.autohide").hide('slow');
            $j('#toggle-online-users').removeClass('active');
            $field.val('');
            $j.getJSON(portal_url + '/content-transform?', {text: text}, function (data) {
                message = $msg({to: recipient, type: 'chat'}).c('body').t(data.text);
                jarnxmpp.connection.send(message);
            });
            e.preventDefault();
        });*/




    
    
   
});