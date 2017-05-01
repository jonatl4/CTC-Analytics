import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def py_mail(SUBJECT, BODY, TO, FROM):
    """With this function we send out our html email"""
    
    # Create message container - the correct MIME type is multipart/alternative here!
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = FROM
    MESSAGE.preamble = """
        Your mail reader does not support the report format.
        Please visit us <a href="http://www.mysite.com">online</a>!"""
    
    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')
    
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)
    
    # The actual sending of the e-mail
    server = smtplib.SMTP('smtp.gmail.com:587')
    
    # Print debugging output when testing
    if __name__ == "__main__":
        server.set_debuglevel(1)
    
    # Credentials (if needed) for sending the mail
        password = "Anubis1995"

server.starttls()
server.login("rsdihom@gmail.com","Anubis1995")
server.sendmail("rsdihom@gmai.com", ["rsdihom@gmail.com"], MESSAGE.as_string())
server.quit()

if __name__ == "__main__":
    """Executes if the script is run as main script (for testing purposes)"""
    email_text = """<!doctype html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <title>Simple Transactional Email</title>
        <style>
        /* -------------------------------------
        GLOBAL RESETS
        ------------------------------------- */
        img {
        border: none;
        -ms-interpolation-mode: bicubic;
        max-width: 100%; }
        body {
        background-color: #f6f6f6;
        font-family: sans-serif;
        -webkit-font-smoothing: antialiased;
        font-size: 14px;
        line-height: 1.4;
        margin: 0;
        padding: 0;
        -ms-text-size-adjust: 100%;
        -webkit-text-size-adjust: 100%; }
        table {
        border-collapse: separate;
        mso-table-lspace: 0pt;
        mso-table-rspace: 0pt;
        width: 100%; }
        table td {
        font-family: sans-serif;
        font-size: 14px;
        vertical-align: top; }
        /* -------------------------------------
        BODY & CONTAINER
        ------------------------------------- */
        .body {
        background-color: #f6f6f6;
        width: 100%; }
        /* Set a max-width, and make it display as block so it will automatically stretch to that width, but will also shrink down on a phone or something */
        .container {
        display: block;
        Margin: 0 auto !important;
        /* makes it centered */
        max-width: 580px;
        padding: 10px;
        width: 580px; }
        /* This should also be a block element, so that it will fill 100% of the .container */
        .content {
        box-sizing: border-box;
        display: block;
        Margin: 0 auto;
        max-width: 580px;
        padding: 10px; }
        /* -------------------------------------
        HEADER, FOOTER, MAIN
        ------------------------------------- */
        .main {
        background: #fff;
        border-radius: 3px;
        width: 100%; }
        .wrapper {
        box-sizing: border-box;
        padding: 20px; }
        .footer {
        clear: both;
        padding-top: 10px;
        text-align: center;
        width: 100%; }
        .footer td,
        .footer p,
        .footer span,
        .footer a {
        color: #999999;
        font-size: 12px;
        text-align: center; }
        /* -------------------------------------
        TYPOGRAPHY
        ------------------------------------- */
        h1,
        h2,
        h3,
        h4 {
        color: #000000;
        font-family: sans-serif;
        font-weight: 400;
        line-height: 1.4;
        margin: 0;
        Margin-bottom: 30px; }
        h1 {
        font-size: 35px;
        font-weight: 300;
        text-align: center;
        text-transform: capitalize; }
        p,
        ul,
        ol {
        font-family: sans-serif;
        font-size: 14px;
        font-weight: normal;
        margin: 0;
        Margin-bottom: 15px; }
        p li,
        ul li,
        ol li {
        list-style-position: inside;
        margin-left: 5px; }
        a {
        color: #3498db;
        text-decoration: underline; }
        /* -------------------------------------
        BUTTONS
        ------------------------------------- */
        .btn {
        box-sizing: border-box;
        width: 100%; }
        .btn > tbody > tr > td {
        padding-bottom: 15px; }
        .btn table {
        width: auto; }
        .btn table td {
        background-color: #ffffff;
        border-radius: 5px;
        text-align: center; }
        .btn a {
        background-color: #ffffff;
        border: solid 1px #3498db;
        border-radius: 5px;
        box-sizing: border-box;
        color: #3498db;
        cursor: pointer;
        display: inline-block;
        font-size: 14px;
        font-weight: bold;
        margin: 0;
        padding: 12px 25px;
        text-decoration: none;
        text-transform: capitalize; }
        .btn-primary table td {
        background-color: #3498db; }
        .btn-primary a {
        background-color: #3498db;
        border-color: #3498db;
        color: #ffffff; }
        /* -------------------------------------
        OTHER STYLES THAT MIGHT BE USEFUL
        ------------------------------------- */
        .last {
        margin-bottom: 0; }
        .first {
        margin-top: 0; }
        .align-center {
        text-align: center; }
        .align-right {
        text-align: right; }
        .align-left {
        text-align: left; }
        .clear {
        clear: both; }
        .mt0 {
        margin-top: 0; }
        .mb0 {
        margin-bottom: 0; }
        .preheader {
        color: transparent;
        display: none;
        height: 0;
        max-height: 0;
        max-width: 0;
        opacity: 0;
        overflow: hidden;
        mso-hide: all;
        visibility: hidden;
        width: 0; }
        .powered-by a {
        text-decoration: none; }
        hr {
        border: 0;
        border-bottom: 1px solid #f6f6f6;
        Margin: 20px 0; }
        /* -------------------------------------
        RESPONSIVE AND MOBILE FRIENDLY STYLES
        ------------------------------------- */
        @media only screen and (max-width: 620px) {
        table[class=body] h1 {
        font-size: 28px !important;
        margin-bottom: 10px !important; }
        table[class=body] p,
        table[class=body] ul,
        table[class=body] ol,
        table[class=body] td,
        table[class=body] span,
        table[class=body] a {
        font-size: 16px !important; }
        table[class=body] .wrapper,
        table[class=body] .article {
        padding: 10px !important; }
        table[class=body] .content {
        padding: 0 !important; }
        table[class=body] .container {
        padding: 0 !important;
        width: 100% !important; }
        table[class=body] .main {
        border-left-width: 0 !important;
        border-radius: 0 !important;
        border-right-width: 0 !important; }
        table[class=body] .btn table {
        width: 100% !important; }
        table[class=body] .btn a {
        width: 100% !important; }
        table[class=body] .img-responsive {
        height: auto !important;
        max-width: 100% !important;
        width: auto !important; }}
        /* -------------------------------------
        PRESERVE THESE STYLES IN THE HEAD
        ------------------------------------- */
        @media all {
        .ExternalClass {
        width: 100%; }
        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {
        line-height: 100%; }
        .apple-link a {
        color: inherit !important;
        font-family: inherit !important;
        font-size: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
        text-decoration: none !important; }
        .btn-primary table td:hover {
        background-color: #34495e !important; }
        .btn-primary a:hover {
        background-color: #34495e !important;
        border-color: #34495e !important; } }
        </style>
        </head>
        <body class="">
        <table border="0" cellpadding="0" cellspacing="0" class="body">
        <tr>
        <td>&nbsp;</td>
        <td class="container">
        <div class="content">
        
        <!-- START CENTERED WHITE CONTAINER -->
        <span class="preheader">This is preheader text. Some clients will show this text as a preview.</span>
        <table class="main">
        
        <!-- START MAIN CONTENT AREA -->
        <tr>
        <td class="wrapper">
        <table border="0" cellpadding="0" cellspacing="0">
        <tr>
        <td>
        <p>Hi there,</p>
        <p>Sometimes you just want to send a simple HTML email with a simple design and clear call to action. This is it.</p>
        <table border="0" cellpadding="0" cellspacing="0" class="btn btn-primary">
        <tbody>
        <tr>
        <td align="left">
        <table border="0" cellpadding="0" cellspacing="0">
        <tbody>
        <tr>
        <td> <a href="http://htmlemail.io" target="_blank">Call To Action</a> </td>
        </tr>
        </tbody>
        </table>
        </td>
        </tr>
        </tbody>
        </table>
        <p>This is a really simple email template. Its sole purpose is to get the recipient to click the button with no distractions.</p>
        <p>Good luck! Hope it works.</p>
        </td>
        </tr>
        </table>
        </td>
        </tr>
        
        <!-- END MAIN CONTENT AREA -->
        </table>
        
        <!-- START FOOTER -->
        <div class="footer">
        <table border="0" cellpadding="0" cellspacing="0">
        <tr>
        <td class="content-block">
        <span class="apple-link">Company Inc, 3 Abbey Road, San Francisco CA 94102</span>
        <br> Don't like these emails? <a href="http://i.imgur.com/CScmqnj.gif">Unsubscribe</a>.
        </td>
        </tr>
        <tr>
        <td class="content-block powered-by">
        Powered by <a href="http://htmlemail.io">HTMLemail</a>.
        </td>
        </tr>
        </table>
        </div>
        
        <!-- END FOOTER -->
        
        <!-- END CENTERED WHITE CONTAINER --></div>
        </td>
        <td>&nbsp;</td>
        </tr>
        </table>
        </body>
        </html>"""

html_test = """<!DOCTYPE html>
    <meta charset="utf-8">
    <style>
    body{
    width:1060px;
    margin:50px auto;
    }
    path {  stroke: #fff; }
    path:hover {  opacity:0.9; }
    rect:hover {  fill:blue; }
    .axis {  font: 10px sans-serif; }
    .legend tr{    border-bottom:1px solid grey; }
    .legend tr:first-child{    border-top:1px solid grey; }
    
    .axis path,
    .axis line {
    fill: none;
    stroke: #000;
    shape-rendering: crispEdges;
    }
    
    .x.axis path {  display: none; }
    .legend{
    margin-bottom:76px;
    display:inline-block;
    border-collapse: collapse;
    border-spacing: 0px;
    }
    .legend td{
    padding:4px 5px;
    vertical-align:bottom;
    }
    .legendFreq, .legendPerc{
    align:right;
    width:50px;
    }
    
    </style>
    <body>
    <div id='dashboard'>
    </div>
    <script src="http://d3js.org/d3.v3.min.js"></script>
    <script>
    function dashboard(id, fData){
    var barColor = 'steelblue';
    function segColor(c){ return {low:"#807dba", mid:"#e08214",high:"#41ab5d"}[c]; }
    
    // compute total for each state.
    fData.forEach(function(d){d.total=d.freq.low+d.freq.mid+d.freq.high;});
    
    // function to handle histogram.
    function histoGram(fD){
    var hG={},    hGDim = {t: 60, r: 0, b: 30, l: 0};
    hGDim.w = 500 - hGDim.l - hGDim.r,
    hGDim.h = 300 - hGDim.t - hGDim.b;
    
    //create svg for histogram.
    var hGsvg = d3.select(id).append("svg")
    .attr("width", hGDim.w + hGDim.l + hGDim.r)
    .attr("height", hGDim.h + hGDim.t + hGDim.b).append("g")
    .attr("transform", "translate(" + hGDim.l + "," + hGDim.t + ")");
    
    // create function for x-axis mapping.
    var x = d3.scale.ordinal().rangeRoundBands([0, hGDim.w], 0.1)
    .domain(fD.map(function(d) { return d[0]; }));
    
    // Add x-axis to the histogram svg.
    hGsvg.append("g").attr("class", "x axis")
    .attr("transform", "translate(0," + hGDim.h + ")")
    .call(d3.svg.axis().scale(x).orient("bottom"));
    
    // Create function for y-axis map.
    var y = d3.scale.linear().range([hGDim.h, 0])
    .domain([0, d3.max(fD, function(d) { return d[1]; })]);
    
    // Create bars for histogram to contain rectangles and freq labels.
    var bars = hGsvg.selectAll(".bar").data(fD).enter()
    .append("g").attr("class", "bar");
    
    //create the rectangles.
    bars.append("rect")
    .attr("x", function(d) { return x(d[0]); })
    .attr("y", function(d) { return y(d[1]); })
    .attr("width", x.rangeBand())
    .attr("height", function(d) { return hGDim.h - y(d[1]); })
    .attr('fill',barColor)
    .on("mouseover",mouseover)// mouseover is defined below.
    .on("mouseout",mouseout);// mouseout is defined below.
    
    //Create the frequency labels above the rectangles.
    bars.append("text").text(function(d){ return d3.format(",")(d[1])})
    .attr("x", function(d) { return x(d[0])+x.rangeBand()/2; })
    .attr("y", function(d) { return y(d[1])-5; })
    .attr("text-anchor", "middle");
    
    function mouseover(d){  // utility function to be called on mouseover.
    // filter for selected state.
    var st = fData.filter(function(s){ return s.State == d[0];})[0],
    nD = d3.keys(st.freq).map(function(s){ return {type:s, freq:st.freq[s]};});
    
    // call update functions of pie-chart and legend.
    pC.update(nD);
    leg.update(nD);
    }
    
    function mouseout(d){    // utility function to be called on mouseout.
    // reset the pie-chart and legend.
    pC.update(tF);
    leg.update(tF);
    }
    
    // create function to update the bars. This will be used by pie-chart.
    hG.update = function(nD, color){
    // update the domain of the y-axis map to reflect change in frequencies.
    y.domain([0, d3.max(nD, function(d) { return d[1]; })]);
    
    // Attach the new data to the bars.
    var bars = hGsvg.selectAll(".bar").data(nD);
    
    // transition the height and color of rectangles.
    bars.select("rect").transition().duration(500)
    .attr("y", function(d) {return y(d[1]); })
    .attr("height", function(d) { return hGDim.h - y(d[1]); })
    .attr("fill", color);
    
    // transition the frequency labels location and change value.
    bars.select("text").transition().duration(500)
    .text(function(d){ return d3.format(",")(d[1])})
    .attr("y", function(d) {return y(d[1])-5; });
    }
    return hG;
    }
    
    // function to handle pieChart.
    function pieChart(pD){
    var pC ={},    pieDim ={w:250, h: 250};
    pieDim.r = Math.min(pieDim.w, pieDim.h) / 2;
    
    // create svg for pie chart.
    var piesvg = d3.select(id).append("svg")
    .attr("width", pieDim.w).attr("height", pieDim.h).append("g")
    .attr("transform", "translate("+pieDim.w/2+","+pieDim.h/2+")");
    
    // create function to draw the arcs of the pie slices.
    var arc = d3.svg.arc().outerRadius(pieDim.r - 10).innerRadius(0);
    
    // create a function to compute the pie slice angles.
    var pie = d3.layout.pie().sort(null).value(function(d) { return d.freq; });
    
    // Draw the pie slices.
    piesvg.selectAll("path").data(pie(pD)).enter().append("path").attr("d", arc)
    .each(function(d) { this._current = d; })
    .style("fill", function(d) { return segColor(d.data.type); })
    .on("mouseover",mouseover).on("mouseout",mouseout);
    
    // create function to update pie-chart. This will be used by histogram.
    pC.update = function(nD){
    piesvg.selectAll("path").data(pie(nD)).transition().duration(500)
    .attrTween("d", arcTween);
    }
    // Utility function to be called on mouseover a pie slice.
    function mouseover(d){
    // call the update function of histogram with new data.
    hG.update(fData.map(function(v){
    return [v.State,v.freq[d.data.type]];}),segColor(d.data.type));
    }
    //Utility function to be called on mouseout a pie slice.
    function mouseout(d){
    // call the update function of histogram with all data.
    hG.update(fData.map(function(v){
    return [v.State,v.total];}), barColor);
    }
    // Animating the pie-slice requiring a custom function which specifies
    // how the intermediate paths should be drawn.
    function arcTween(a) {
    var i = d3.interpolate(this._current, a);
    this._current = i(0);
    return function(t) { return arc(i(t));    };
    }
    return pC;
    }
    
    // function to handle legend.
    function legend(lD){
    var leg = {};
    
    // create table for legend.
    var legend = d3.select(id).append("table").attr('class','legend');
    
    // create one row per segment.
    var tr = legend.append("tbody").selectAll("tr").data(lD).enter().append("tr");
    
    // create the first column for each segment.
    tr.append("td").append("svg").attr("width", '16').attr("height", '16').append("rect")
    .attr("width", '16').attr("height", '16')
    .attr("fill",function(d){ return segColor(d.type); });
    
    // create the second column for each segment.
    tr.append("td").text(function(d){ return d.type;});
    
    // create the third column for each segment.
    tr.append("td").attr("class",'legendFreq')
    .text(function(d){ return d3.format(",")(d.freq);});
    
    // create the fourth column for each segment.
    tr.append("td").attr("class",'legendPerc')
    .text(function(d){ return getLegend(d,lD);});
    
    // Utility function to be used to update the legend.
    leg.update = function(nD){
    // update the data attached to the row elements.
    var l = legend.select("tbody").selectAll("tr").data(nD);
    
    // update the frequencies.
    l.select(".legendFreq").text(function(d){ return d3.format(",")(d.freq);});
    
    // update the percentage column.
    l.select(".legendPerc").text(function(d){ return getLegend(d,nD);});
    }
    
    function getLegend(d,aD){ // Utility function to compute percentage.
    return d3.format("%")(d.freq/d3.sum(aD.map(function(v){ return v.freq; })));
    }
    
    return leg;
    }
    
    // calculate total frequency by segment for all state.
    var tF = ['low','mid','high'].map(function(d){
    return {type:d, freq: d3.sum(fData.map(function(t){ return t.freq[d];}))};
    });
    
    // calculate total frequency by state for all segment.
    var sF = fData.map(function(d){return [d.State,d.total];});
    
    var hG = histoGram(sF), // create the histogram.
    pC = pieChart(tF), // create the pie-chart.
    leg= legend(tF);  // create the legend.
    }
    </script>
    
    <script>
    var freqData=[
    {State:'AL',freq:{low:4786, mid:1319, high:249}}
    ,{State:'AZ',freq:{low:1101, mid:412, high:674}}
    ,{State:'CT',freq:{low:932, mid:2149, high:418}}
    ,{State:'DE',freq:{low:832, mid:1152, high:1862}}
    ,{State:'FL',freq:{low:4481, mid:3304, high:948}}
    ,{State:'GA',freq:{low:1619, mid:167, high:1063}}
    ,{State:'IA',freq:{low:1819, mid:247, high:1203}}
    ,{State:'IL',freq:{low:4498, mid:3852, high:942}}
    ,{State:'IN',freq:{low:797, mid:1849, high:1534}}
    ,{State:'KS',freq:{low:162, mid:379, high:471}}
    ];
    
    dashboard('#dashboard',freqData);
    </script>
    """
emailGraph = """<html>
    <table width="640" border="0" cellspacing="0" cellpadding="20" class="100p" bgcolor="#FFFFFF">
    <tr>
    <td align="center" valign="top">
    <table border="0" cellpadding="0" cellspacing="0" class="100padtopbottom" width="600">
    <tr>
    <td align="left" class="condensed" valign="top">
    <table align="left" border="0" cellpadding="0" cellspacing="0" class="mob-column" width="290">
    <tr>
    <td valign="top" align="center">
    <table border="0" cellspacing="0" cellpadding="0">
    <tr>
    <td valign="top" align="center" class="100padleftright">
    <table border="0" cellspacing="0" cellpadding="0">
    <tr>
    <td width="135" align="center"><a href="#"><img src="images/icon-1.png" border="0" style="display:block;"/></a></td>
    <td width="20"></td>
    <td width="135" align="center"><a href="#"><img src="images/icon-1.png" border="0" style="display:block;"/></a></td>
    </tr>
    </table>
    </td>
    </tr>
    <tr>
    <td height="10"></td>
    </tr>
    <tr>
    <td valign="top" class="100padleftright" align="center">
    <table border="0" cellspacing="0" cellpadding="0">
    <tr>
    <td valign="top" width="135" align="center" style="font-size:16px; color:#2a8e9d;"><font face="'Roboto', Arial, sans-serif">Customise your user messages</font></td>
    <td width="20"></td>
    <td valign="top" width="135" align="center"  style="font-size:16px; color:#2a8e9d;"><font face="'Roboto', Arial, sans-serif">100% unique privacy options</font></td>
    </tr>
    </table>
    </td>
    </tr>
    </table>
    </td>
    </tr>
    </table>
    </td>
    <td width="20" class="hide"></td>
    <td align="left" class="condensed" valign="top">
    <table align="left" border="0" cellpadding="0" cellspacing="0" class="mob-column" width="290">
    <tr>
    <td valign="top" align="center">
    <table border="0" cellspacing="0" cellpadding="0">
    <tr>
    <td valign="top" align="center" class="100padleftright">
    <table border="0" cellspacing="0" cellpadding="0">
    <tr>
    <td width="135" align="center"><a href="#"><img src="images/icon-1.png" border="0" style="display:block;"/></a></td>
    <td width="20"></td>
    <td width="135" align="center"><a href="#"><img src="images/icon-1.png" border="0" style="display:block;"/></a></td>
    </tr>
    </table>
    </td>
    </tr>
    <tr>
    <td height="10"></td>
    </tr>
    <tr>
    <td valign="top" class="100padleftright" align="center">
    <table border="0" cellspacing="0" cellpadding="0">
    <tr>
    <td valign="top" width="135" align="center" style="font-size:16px; color:#2a8e9d;"><font face="'Roboto', Arial, sans-serif">Fully customise your settings</font></td>
    <td width="20"></td>
    <td valign="top" width="135" align="center"  style="font-size:16px; color:#2a8e9d;"><font face="'Roboto', Arial, sans-serif">Upload your product photos</font></td>
    </tr>
    </table>
    </td>
    </tr>
    </table>
    </td>
    </tr>
    </table>
    </td>
    </tr>
    </table>
    </td>
    </tr>
    </table>
    </html>
    """
email_content = """
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>html title</title>
    <div id="doughnutChart" class="chart"></div>
    <style type="text/css" media="screen">
    table{
    background-color: #AAD373;
    empty-cells:hide;
    }
    td.cell{
    background-color: white;
    }
    </style>
    </head>
    <body>
    <table style="border: blue 1px solid;">
    <tr><td class="cell">Cell 1.1</td><td class="cell">Cell 1.2</td></tr>
    <tr><td class="cell">Cell 2.1</td><td class="cell"></td></tr>
    </table>
    </body>
    """

TO = 'rdihom@uci.edu'
FROM ='rsdihom@gmail.com'

py_mail("Test email subject", email_content, TO, FROM)
