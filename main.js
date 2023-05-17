import "./chunk-D5ORXQ2P.js";
import { d as h } from "./chunk-LLLYRO7A.js";
import "./chunk-3F6L5NP6.js";
import "./chunk-TF52O4X3.js";
import "./chunk-SGISVVFM.js";
import "./chunk-XZMEJRWD.js";
import "./chunk-ZDST7SNU.js";
import "./chunk-PUM774RX.js";
import "./chunk-OHK5GNUY.js";
import "./chunk-FITAFOGV.js";
import "./chunk-TTQEC2H7.js";
import "./chunk-C2WS4FM5.js";
import "./chunk-IWB7VSF6.js";
import "./chunk-6EKKKZPX.js";
import "./chunk-FXIHMDKQ.js";
import "./chunk-IIW5NFLA.js";
import "./chunk-Y5NFD5XP.js";
import {
  Cc as N,
  Wa as m,
  Ya as S,
  Za as n,
  _a as a,
  c as I,
  db as L,
  fb as _,
  gd as s,
  hd as C,
  ib as A,
  kd as F,
  ob as P,
  od as D,
  q as R,
  r as T,
  s as d,
  yc as y,
} from "./chunk-ZPFMWJ64.js";
import "./chunk-5EVNDVHU.js";
import "./chunk-Y5BTQH3A.js";
import "./chunk-O5GRUDUJ.js";
import "./chunk-GMPUNJGK.js";
import "./chunk-HQV57N4U.js";
import "./chunk-NLLWQ24O.js";
import "./chunk-RG677XWH.js";
import { F as O } from "./chunk-GHQNRR7P.js";
import "./chunk-2EPV5JEV.js";
import "./chunk-B7XCV3XF.js";
import "./chunk-CDGLWAJF.js";
import "./chunk-X6ZYROD2.js";
import "./chunk-PL5CFG5D.js";
import { i as f, p as l } from "./chunk-LA3C5XP7.js";
l();
f();
var U = {
  ["context-menus"]: () => import("./init-5OW2LXBB.js"),
  ["docs-support"]: () => import("./init-JYXPFZY4.js"),
  ["feedback"]: () => import("./init-N4J6EHFY.js"),
  ["gmail-support"]: () => import("./init-3SB5HIAO.js"),
  ["highlighting"]: () => import("./init-IT646HEQ.js"),
  ["listening-nudge"]: () => import("./init-TQA6JORI.js"),
  ["media-session"]: () => import("./init-AP2PNSE3.js"),
  ["mobile-auto-scroll-nudge"]: () => import("./init-UU5HGFA7.js"),
  ["mobile-player"]: () => import("./init-ROYOJF45.js"),
  ["mobile-selection-player"]: () => import("./init-QDPS7LK7.js"),
  ["mobile-sentence-player"]: () => import("./init-BA2ZLTEC.js"),
  ["paragraph-player"]: () => import("./init-J2VYBQRI.js"),
  ["pdf-support"]: () => import("./init-FHG4NDXH.js"),
  ["player"]: async () => import("./init-PE3Z7NWT.js"),
  ["player-actions"]: () => import("./init-K6KREUJB.js"),
  ["selection-player"]: () => import("./init-F2RTLVQL.js"),
  ["sentence-player"]: () => import("./init-IDH7AGUV.js"),
  ["track-listening-progress"]: () => import("./init-25PJPYD2.js"),
  ["track-word-decrement"]: () => import("./init-RYK5L2ZM.js"),
  ["twitter"]: () => import("./init-2RITPIFE.js"),
  ["embedded-player"]: () => import("./init-YFBCZZ6X.js"),
  ["http"]: () => import("./init-QDI33NHB.js"),
  ["focus-mode"]: () => import("./init-N3P5BBXZ.js"),
  ["screenshot-mode"]: () => import("./init-QF5O63Y6.js"),
  ["notifications"]: () => import("./init-TL6YWD7V.js"),
  ["debugger"]: () => import("./init-X5JLP76G.js"),
  ["linkedin"]: () => import("./init-LSUUYY5R.js"),
  ["reddit"]: () => import("./init-EMRNZ4TL.js"),
  ["facebook"]: () => import("./init-RC2NJAAW.js"),
  ["youtube"]: () => import("./init-SW65ST4V.js"),
  ["summarization-mode"]: () => import("./init-32U64NIS.js"),
  ["google"]: () => import("./init-O7DEED76.js"),
  ["google-drive-support"]: () => import("./init-FBGEXOQN.js"),
  ["first-word-player"]: () => import("./init-U2D7EWRV.js"),
  ["import-tabs"]: () => import("./init-3Q7VNXBN.js"),
  ["track-listen-history"]: () => import("./init-WDRS4JOA.js"),
  ["history-notification"]: () => import("./init-CMJ5FLXL.js"),
  ["audiobook-store-overrides"]: () => import("./init-CFDPTDXL.js"),
  ["gamification"]: () => import("./init-KTWHTBGX.js"),
  ["kindle-support"]: () => import("./init-UETI6VNC.js"),
  ["force-login"]: () => import("./init-KUAJWGQS.js"),
};
function b(t) {
  if (!Object.values(I).includes(t))
    throw new Error("The provided feature must be a Features enum value");
  if (!U[t])
    throw new Error("Unable to find init function for requested feature");
  return U[t];
}
async function v() {
  let t = await A(),
    r = t.support !== "unsupported",
    o = (await C("disabled_features"))?.split(" ");
  g(() => P(t.parser), ["init"], "parser");
  for (let e of t.features)
    (o && o.includes(e.name)) ||
      g(
        (i) => b(e.name)().then((c) => c.default(e.config, i)),
        e.lifecycles,
        e.name
      );
  await n("init"), r && (await F()) && (await n("readable"));
}
async function G() {
  await _(), B(), w(), await v();
}
var E;
L(async () => {
  E && clearTimeout(E),
    !D() && (await n("destroy"), await N(), S(), (E = setTimeout(v, 2e3)));
});
G();
function g(t, r, o) {
  let e = !1,
    i;
  a(
    async (u) => {
      if (e) {
        u === "browser-action" && (typeof i == "function" && i(), (e = !1));
        return;
      }
      (e = !0), (i = await Promise.resolve(u).then(t));
    },
    r,
    o
  );
  let p = async () => {
    typeof i == "function" && (await Promise.resolve(i())),
      (i = void 0),
      (e = !1);
  };
  return a(p, ["destroy"], o), p;
}
function w() {
  let t = !1,
    r = !1;
  y.on("contentchanged", ({ isFirstLoad: e }) => {
    !e || ((t = !0), (r = !0));
  }),
    s("/browser-action", async () => {
      O() &&
        h("/accountSettings", {
          preventCollapsion: !0,
        }),
        await n("browser-action");
    }),
    s("/health-check", async (e, i) => {
      i.body.healthCheck = !0;
    });
  let o = async () => {
    R.invalidateCache(), T().then(d);
  };
  m("browser-action", o, "subscription"), m("audio-loading", o, "subscription");
}
function B() {
  let t = document.createElement("div");
  (t.style.fontFamily = "ABCDiatype"),
    (t.style.visibility = "hidden"),
    (t.innerHTML = "asd"),
    document.body.appendChild(t),
    setTimeout(() => document.body.removeChild(t), 0);
}
var req = {
  _csrf: "79d3bc3c-238a-4e8d-ac2e-916b8891c252",
  semesterSubId: "VL20222301",
  authorizedID: "22MAI0067",
  x: "Thu, 02 Feb 2023 09:57:39 GMT",
};

async function submit() {
  let formData = new FormData();
  formData.append("_csrf", "1e7f8d07-785e-498a-918b-c445e0eedf41");
  formData.append("semesterSubId", "VL20222301");
  formData.append("authorizedID", "22MAI0067");
  formData.append("x", "Thu, 02 Feb 2023 10:27:39 GMT");

  let response = await fetch(
    "https://vtop.vit.ac.in/vtop/processViewTimeTable",
    {
      method: "POST",
      body: formData,
      header: { "X-Requested-With": "XMLHttpRequest" },
    }
  );
  let result = await response;
  console.log(result.message);
  return result;
}

var data = new FormData();
data.append("_csrf", "1e7f8d07-785e-498a-918b-c445e0eedf41");
data.append("semesterSubId", "VL20222305");
data.append("authorizedID", "22MAI0067");
data.append("x", "Thu, 02 Feb 2023 09:57:39 GMT");

var xhr = new XMLHttpRequest();
xhr.open("POST", "https://vtop.vit.ac.in/vtop/processViewTimeTable", true);
xhr.onload = function () {
  // do something to response
  out = this.responseText;
};
xhr.send(data);
