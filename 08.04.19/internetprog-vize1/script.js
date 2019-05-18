var say =5;
var indirme;
var sure;
function baslat(){
    indirme = setTimeout(dosyaindirme,5000);
    sureyisay();
    sure = setInterval(sureyisay,1000);
}
function dosyaindirme() {
    window.alert("Dosya indirme işlemi başladı ...");
    document.getElementById("para").innerHTML = "";
    say=5;
}
function sureyisay() {
    document.getElementById("para").innerHTML="Dosya "+say+" Saniye içinde inecek";
    say --;
    if (say==0){
        clearInterval(sure);
    }
}
function islemleri_durdur() {
    clearInterval(sure);
    clearTimeout(indirme);
    document.getElementById("para").innerHTML="Dosya indirmesi durduruldu!";
    say=5;
}