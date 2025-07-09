"use strict";
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype);
    return g.next = verb(0), g["throw"] = verb(1), g["return"] = verb(2), typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var __asyncValues = (this && this.__asyncValues) || function (o) {
    if (!Symbol.asyncIterator) throw new TypeError("Symbol.asyncIterator is not defined.");
    var m = o[Symbol.asyncIterator], i;
    return m ? m.call(o) : (o = typeof __values === "function" ? __values(o) : o[Symbol.iterator](), i = {}, verb("next"), verb("throw"), verb("return"), i[Symbol.asyncIterator] = function () { return this; }, i);
    function verb(n) { i[n] = o[n] && function (v) { return new Promise(function (resolve, reject) { v = o[n](v), settle(resolve, reject, v.done, v.value); }); }; }
    function settle(resolve, reject, d, v) { Promise.resolve(v).then(function(v) { resolve({ value: v, done: d }); }, reject); }
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.advancedFetch = advancedFetch;
var proxy_from_env_1 = require("proxy-from-env");
var undici_1 = require("undici");
var stream_1 = require("stream");
/**
 * Advanced fetch with automatic proxy-from-env and undici ProxyAgent support.
 * @param url - The target URL.
 * @param options - Options for undici request (headers, method, etc).
 * @returns undici response object
 */
function advancedFetch(url_1) {
    return __awaiter(this, arguments, void 0, function (url, options) {
        var proxy, agent, dispatcher, reqOptions;
        if (options === void 0) { options = {}; }
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    proxy = (0, proxy_from_env_1.getProxyForUrl)(url);
                    agent = proxy ? new undici_1.ProxyAgent(proxy) : undefined;
                    dispatcher = agent || undefined;
                    reqOptions = __assign(__assign({}, options), { dispatcher: dispatcher });
                    return [4 /*yield*/, (0, undici_1.request)(url, reqOptions)];
                case 1: return [2 /*return*/, _a.sent()];
            }
        });
    });
}
// Example usage:
var targetUrl = 'https://remote-mcp-server-authless-2.hrwnwbyzt.workers.dev/sse';
console.log('🔍 Proxy:', (0, proxy_from_env_1.getProxyForUrl)(targetUrl) || 'No proxy used');
console.log('🌐 Connecting to SSE URL:', targetUrl);
(function () { return __awaiter(void 0, void 0, void 0, function () {
    var _a, statusCode, body, decoder, stream, _b, stream_2, stream_2_1, chunk, text, e_1_1;
    var _c, e_1, _d, _e;
    return __generator(this, function (_f) {
        switch (_f.label) {
            case 0: return [4 /*yield*/, advancedFetch(targetUrl, {
                    method: 'GET',
                    headers: {
                        'Accept': 'text/event-stream',
                    },
                })];
            case 1:
                _a = _f.sent(), statusCode = _a.statusCode, body = _a.body;
                if (statusCode !== 200) {
                    console.error("\u274C Failed to connect: HTTP ".concat(statusCode));
                    process.exit(1);
                }
                console.log('✅ Connected. Streaming SSE data:\n');
                decoder = new TextDecoder();
                stream = stream_1.Readable.from(body);
                _f.label = 2;
            case 2:
                _f.trys.push([2, 7, 8, 13]);
                _b = true, stream_2 = __asyncValues(stream);
                _f.label = 3;
            case 3: return [4 /*yield*/, stream_2.next()];
            case 4:
                if (!(stream_2_1 = _f.sent(), _c = stream_2_1.done, !_c)) return [3 /*break*/, 6];
                _e = stream_2_1.value;
                _b = false;
                chunk = _e;
                text = decoder.decode(chunk, { stream: true });
                process.stdout.write(text);
                _f.label = 5;
            case 5:
                _b = true;
                return [3 /*break*/, 3];
            case 6: return [3 /*break*/, 13];
            case 7:
                e_1_1 = _f.sent();
                e_1 = { error: e_1_1 };
                return [3 /*break*/, 13];
            case 8:
                _f.trys.push([8, , 11, 12]);
                if (!(!_b && !_c && (_d = stream_2.return))) return [3 /*break*/, 10];
                return [4 /*yield*/, _d.call(stream_2)];
            case 9:
                _f.sent();
                _f.label = 10;
            case 10: return [3 /*break*/, 12];
            case 11:
                if (e_1) throw e_1.error;
                return [7 /*endfinally*/];
            case 12: return [7 /*endfinally*/];
            case 13: return [2 /*return*/];
        }
    });
}); })();
