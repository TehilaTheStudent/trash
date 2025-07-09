import { getProxyForUrl } from 'proxy-from-env';
import { request as undiciRequest, ProxyAgent } from 'undici';
import { Readable } from 'stream';
/**
 * Advanced fetch with automatic proxy-from-env and undici ProxyAgent support.
 * @param url - The target URL.
 * @param options - Options for undici request (headers, method, etc).
 * @returns undici response object
 */
/**
 * Advanced fetch with automatic proxy-from-env and undici ProxyAgent support.
 * @param url - The target URL.
 * @param options - Options for undici request (headers, method, etc).
 * @returns undici response object
 */
export async function advancedFetch(url, options = {}) {
    const proxy = getProxyForUrl(url);
    const agent = proxy ? new ProxyAgent(proxy) : undefined;
    const dispatcher = agent || undefined;
    const reqOptions = { ...options, dispatcher };
    return await undiciRequest(url, reqOptions);
}
// Example usage:
const targetUrl = 'https://remote-mcp-server-authless-2.hrwnwbyzt.workers.dev/sse';
console.log('🔍 Proxy:', getProxyForUrl(targetUrl) || 'No proxy used');
console.log('🌐 Connecting to SSE URL:', targetUrl);
(async () => {
    const { statusCode, body } = await advancedFetch(targetUrl, {
        method: 'GET',
        headers: {
            'Accept': 'text/event-stream',
        },
    });
    if (statusCode !== 200) {
        console.error(`❌ Failed to connect: HTTP ${statusCode}`);
        process.exit(1);
    }
    console.log('✅ Connected. Streaming SSE data:\n');
    const decoder = new TextDecoder();
    const stream = Readable.from(body);
    for await (const chunk of stream) {
        // chunk is Buffer when using Node.js streams
        const text = decoder.decode(chunk, { stream: true });
        process.stdout.write(text);
    }
})();
