<#macro page_content>
    Empty Page
</#macro>

<#macro page_overlay>
    base overlay content
</#macro>

<#macro pagejs>

</#macro>

<#macro display_page>

    <!DOCTYPE html>
    <html>
        <head>
            <title>TerreXplor</title>

            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

            <link rel="stylesheet" href="/css/vendor.css">
            <link rel="stylesheet" href="/css/app.css">
        </head>
        <body>
            <div id="app-nav-bar">
                Navbar
            </div>
            <div id="page-container">
                <@page_content/>
            </div>
            <div id="page-overlay">
                <div class="page-overlay-shadow">

                </div>
                <div class="page-overlay-window">
                    <@page_overlay/>
                </div>
            </div>

            <script src="/js/vendor.js"></script>
            <script src="/js/app.js"></script>
            <@pagejs/>
        </body>
    </html>

</#macro>
