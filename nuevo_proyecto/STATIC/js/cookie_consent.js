(function(){
    const CONSENT_NAME = "_ga_consent"
    const ONE_YEAR = 60 * 60 *24 * 365

    function getCookie(name){
      return document.cookie  
        .split ("; ")
        .find(row => row.startsWith(name + "="))
        ?.split ("=")[1]
    }


if (getCookie(CONSENT_NAME) === "true"){
   loadGA();
   return;
}

const banner = document.getElementById("cookie-banner");
banner.style.display = "block"

document.getElementById("btn-accept").addEventListener("click", () => {
    document.cookie = `${CONSENT_NAME}=true; max-age=${ONE_YEAR}; path=/; samesite=Lax`;
    loadGA();
    banner.remove();
});
document.getElementById("btn-reject").addEventListener("click", () => {
    banner.remove();
    document.cookie = `${CONSENT_NAME}=false; max-age=${ONE_YEAR}; path=/; samesite=Lax`;

});

function loadGA(){
    if(window.GA_INITIALIZED) return;
    window.GA_INITIALIZED =true;

    const s = document.createElement("script");
    s.src = "https://googletagmanager.com/gtag/js?id=G-XXXX"
    // G-XXXX = la id proporcionada por GA para tus admisiones
    s.async = true;
    document.head.appendChild(s);

    window.dataLayer = window.dataLayer || [];
    function gtag() {dataLayer.push(arguments);}
    gtag('js', new Date ());
    gtag('config', 'G-XXXX', {anonymaze_ip});
}

}());