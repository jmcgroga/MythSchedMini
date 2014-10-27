;MythSchedMini = {
    RELOAD: true,
    INTERVAL: 30000,
    SUSPEND: false,
    clear: function() {
        $('#backend_status').html('');
    },
    showError: function(text) {
        $('#backend_status').html(text);
        $('#backend_status').css('color', 'red')
    },
    showWarning: function(text) {
        $('#backend_status').html(text);
        $('#backend_status').css('color', 'goldenrod')
    },
    backendStatus: function() {
        $.getJSON( "backend_status", function() {
            console.log( "success" );
        }).done(function(data) {
            console.log( "second success" );
            if (data.status) {
                if (data.status == 'Error') {
                    MythSchedMini.showError('Backend Not Running')
                } else if (data.status == 'Okay') {
                    MythSchedMini.clear();
                } else {
                    MythSchedMini.showWarning("Unknown status message: '" + data.status + '"');
                }
            } else {
                MythSchedMini.showError("Error 'status' not returned");
            }
        }).fail(function() {
            MythSchedMini.showError('Error Requesting Status');
        }).always(function() {
        });
    },
    reload: function() {
        if (MythSchedMini.SUSPEND) {
            MythSchedMini.SUSPEND = false;
            setTimeout(MythSchedMini.reload, MythSchedMini.INTERVAL);
        } else {
            $.getJSON( "poke", function() {
                location.reload();
            }).fail(function() {
                MythSchedMini.showError('Error Requesting Status');
            }).always(function() {
                if (MythSchedMini.RELOAD) {
                    setTimeout(MythSchedMini.reload, MythSchedMini.INTERVAL);
                }
            });
        }
    },
    startReloadTimer: function() {
        MythSchedMini.RELOAD = true;
        setTimeout(MythSchedMini.reload, MythSchedMini.INTERVAL);
    },
    stopReloadTimer: function() {
        MythSchedMini.RELOAD = false;
    }
};
