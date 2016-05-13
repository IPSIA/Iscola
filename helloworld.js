/* global Module */

/* Magic Mirror
 * Module: HelloWorld
 *
 * By Michael Teeuw http://michaelteeuw.nl
 * MIT Licensed.
 */


Module.register("helloworld",{

	// Default module config.
	defaults: {
		text: "Hello World!"
	},


    
	// Override dom generator.
	getDom: function() {
		var wrapper = document.createElement("div");
	    // var jsFileLocation = $('script[src*=example]').attr('src'); 
	    // wrapper.innerHTML = jsFileLocation;
	    var scriptEls = document.getElementsByTagName( 'script' );
	    var thisScriptEl = scriptEls[scriptEls.length - 1];
	    var scriptPath = thisScriptEl.src;
	    var scriptFolder = scriptPath.substr(0, scriptPath.lastIndexOf( '/' )+1 );
	    wrapper.innerHTML = scriptFolder+'foto.jpg';

	    // this.file('prova.gg')
	    
	    console.log("__dirname = %s", window.location.pathname);

	    // // lets use a namespace to avoid globals.
	    // var myApp = {
	    // 	// still need to set this when DOM/body is ready
	    // 	rootContext: document.body.getAttribute("data-root"),
	    // 	getContext: function( src ) {
	    // 	    return this.rootContext + src;
	    // 	}
	    // }
	    
	    var img = document.createElement("img");
    // img.src = myApp.getContext( 'foto.jpg' );  //'foto.jpg';
	    img.src = scriptFolder+'foto.jpg';


    img.width = 500;
	    img.height = 300;
	    img.style.position = "absolute";
        img.style.top = '100px';
        img.style.left = '500px';
	    img.alt = 'Google Logo';

    // This next line will just add it to the <body> tag
    document.body.appendChild(img);
	    return wrapper;
	}
});
