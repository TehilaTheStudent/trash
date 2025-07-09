import http from 'http';
import httpProxy from 'http-proxy';
import net from 'net';
import { parse } from 'url';

const proxy = httpProxy.createProxyServer({
  changeOrigin: false,
  prependPath: false,
  ignorePath: true,
  selfHandleResponse: false
});

proxy.on('proxyReq', (proxyReq, req) => {
  console.log(`[proxyReq] ${req.method} ${req.url}`);
});

proxy.on('proxyRes', (proxyRes, req) => {
  console.log(`[proxyRes] ${req.method} ${req.url} -> ${proxyRes.statusCode}`);
});

proxy.on('error', (err, req, res) => {
  console.error(`[proxy error] ${err.message}`);
  if (!res.headersSent) {
    res.writeHead(502);
  }
  res.end('Proxy error.');
});

const server = http.createServer((req, res) => {
  const parsed = parse(req.url);
  const target = `${parsed.protocol}//${parsed.host}`;
  console.log(`[incoming] ${req.method} ${req.url} -> forwarding to ${target}`);
  proxy.web(req, res, { target });
});

// Handle HTTPS CONNECT requests (tunneling)
server.on('connect', (req, clientSocket, head) => {
  const [host, port] = req.url.split(':');
  console.log(`[connect] HTTPS tunnel to ${host}:${port}`);

  const serverSocket = net.connect(port, host, () => {
    clientSocket.write('HTTP/1.1 200 Connection Established\r\n\r\n');
    serverSocket.write(head);
    serverSocket.pipe(clientSocket);
    clientSocket.pipe(serverSocket);
  });

  serverSocket.on('error', (err) => {
    console.error(`[tunnel error] ${err.message}`);
    clientSocket.end('HTTP/1.1 500 Internal Server Error\r\n\r\n');
  });
});

server.listen(3128, () => {
  console.log('🌐 Generic proxy with HTTPS CONNECT listening at http://localhost:3128');
});
