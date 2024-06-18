const sessionStorage = window.sessionStorage ;
const localStorage = window.localStorage ; 

const util = {
    sessionSet(key,value){
        sessionStorage.setItem(key,value);
    },
    sessionGet(key){
        return sessionStorage.getItem(key);
    },
    sessionRemove(key){
        sessionStorage.removeItem(key);
    },
    localStorageSet(){
        localStorage.setItem(key,value);
    },
    localStorageRemove(key){
        localStorage.removeItem(key);
    },
}


export default util;