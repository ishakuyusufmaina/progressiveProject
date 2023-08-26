import { initializeApp } from "https://www.gstatic.com/firebasejs/9.8.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.8.1/firebase-analytics.js";
import {getFirestore, doc, setDoc, getDoc } from "https://www.gstatic.com/firebasejs/9.8.1/firebase-firestore.js";
import {getAuth, GoogleAuthProvider, signInWithRedirect, createUserWithEmailAndPassword} from "https:/www.gstatic.com/firebasejs/9.8.1/firebase-auth.js";
import {getDatabase, ref, set, onValue} from "https:/www.gstatic.com/firebasejs/9.8.1/firebase-database.js";
// TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyBTaxrXnhszPMsLvFryQC7K9dFTukO-0p8",
    authDomain: "icodemy-b08eb.firebaseapp.com",
    projectId: "icodemy-b08eb",
    storageBucket: "icodemy-b08eb.appspot.com",
    messagingSenderId: "1025768308242",
    appId: "1:1025768308242:web:c72fde01cb75ab6119a2cb",
    measurementId: "G-02BCFHE7PQ",
    databaseURL: "https://icodemy-b08eb-default-rtdb.firebaseio.com/"
  };

  // Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const db = getFirestore(app);
const rdb = getDatabase(app);
alert("end of firebase setup");
alert("rtd object: " + rdb);
const remoteBoardRef = ref(rdb, "boards/b1");
alert(remoteBoardRef);

const intface = document.getElementById("interface");
const board = document.getElementById("board");
intface.addEventListener("input", ()=>{
   // board.innerHTML = intface.textContent;
})

const updateBtn = document.getElementById("update-btn");
updateBtn.addEventListener("click", ()=>{
  set(remoteBoardRef, {
    htmlSource: intface.textContent
  })
})

onValue(remoteBoardRef, (snapshot)=>{
  let data = snapshot.val();
  let htmlSrc = data.htmlSource;
  board.innerHTML = htmlSrc;
  intface.innerText = htmlSrc;
});


//authentication 
const auth = getAuth(app);
const provider = new GoogleAuthProvider();
let body = document.body;
let loginContainer = document.createElement("div");
body.append(loginContainer);
loginContainer.innerHTML = "<h3>Login with Google</h3>";
let loginBtn = document.createElement("button");
loginContainer.appendChild(loginBtn);
loginBtn.innerHTML = "Login";
loginBtn.setAttribute("click", ()=>{
  signInWithRedirect(auth, provider);
});
