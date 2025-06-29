import requests
import json

plugins_names = [
  "feishu_robot",
  "tehila-inputs-id",
  "published.CodeArts_Governance.CodeArts_Governance_SCA_Binary",
  "CI-UpdateChangeRequestMetadata",
  "merge_merge_request",
  "DeployMicroserviceInstance",
  "CI-UpgradeChangeRequestEntity",
  "terraform_deploy_plugin",
  "official_devcloud_codeCheck",
  "official_devcloud_cloudBuild",
  "official_third_part_invoke",
  "official_docker",
  "official_artifact_download",
  "published.HuaweiCloudIntel-CAE.official_cae_cross_account",
  "fast-create",
  "my-uniqu-id",
  "official_devcloud_checkpoint",
  "official_devcloud_subPipeline",
  "official_devcloud_createTag",
  "official_kubernetes_release",
  "official_microservice_release",
  "official_docker_executor",
  "official_shell_plugin",
  "download-obs",
  "upload-obs",
  "official_devcloud_cloudBuild_template",
  "published.HuaweiCloud-CAE.official_cae_release",
  "official_developer_debug",
  "official_mvn_dependency",
  "official_devcloud_jenkins",
  "official_branch_change_check",
  "official_gate_source_dependency",
  "official_release_executor",
  "official_devcloud_apiTest_template",
  "official_devcloud_apiTest",
  "official_git_clone",
  "official_merge_default_branch",
  "official_merge_release_branch",
  "official_create_release_branch",
  "official_devcloud_delay",
  "official_devcloud_deploy_template",
  "official_devcloud_codeCheck_template",
  "official_gate_validation",
  "official_devcloud_deploy"
]


url = "https://cloudpipeline-ext.ap-southeast-3.myhuaweicloud.com/v1/9f1a017e31a04489a56572a559924f7c/agent-plugin/plugin-input"

for plugin_name in plugins_names:   
    payload = json.dumps([
    {
        "plugin_name": plugin_name,
        "display_name": "",
        "version": "",
        "plugin_attribution": "",
        "version_attribution": ""
    }
    ])
    headers = {
    'x-auth-token': 'MIIQWwYJKoZIhvcNAQcCoIIQTDCCEEgCAQExDTALBglghkgBZQMEAgEwgg5tBgkqhkiG9w0BBwGggg5eBIIOWnsidG9rZW4iOnsiZXhwaXJlc19hdCI6IjIwMjUtMDYtMTRUMTA6MDg6MTMuMzgwMDAwWiIsIm1ldGhvZHMiOlsicGFzc3dvcmQiXSwiY2F0YWxvZyI6W10sInJvbGVzIjpbeyJuYW1lIjoicmVhZG9ubHkiLCJpZCI6IjAifSx7Im5hbWUiOiJ0ZV9hZG1pbiIsImlkIjoiMCJ9LHsibmFtZSI6ImFwaWdfYWRtIiwiaWQiOiIwIn0seyJuYW1lIjoic2VydmVyX2FkbSIsImlkIjoiMCJ9LHsibmFtZSI6InJkc19hZG0iLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jc2JzX3JlcF9hY2NlbGVyYXRpb24iLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3NfZGlza0FjYyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Rzc19tb250aCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX29ic19kZWVwX2FyY2hpdmUiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hX2NuLXNvdXRoLTRjIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZGVjX21vbnRoX3VzZXIiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jYnJfc2VsbG91dCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Vjc19vbGRfcmVvdXJjZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2V2c19Sb3lhbHR5IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfd2VsaW5rYnJpZGdlX2VuZHBvaW50X2J1eSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Nicl9maWxlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZG1zLXJvY2tldG1xNS1iYXNpYyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Rtcy1rYWZrYTMiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9vYnNfZGVjX21vbnRoIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY3Nic19yZXN0b3JlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY2JyX3Ztd2FyZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2lkbWVfbWJtX2ZvdW5kYXRpb24iLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3NfYzZhIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfbXVsdGlfYmluZCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Ntbl9jYWxsbm90aWZ5IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfTWFwX2JldGEiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hX2FwLXNvdXRoZWFzdC0zZCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NzYnNfcHJvZ3Jlc3NiYXIiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jZXNfcmVzb3VyY2Vncm91cF90YWciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3Nfb2ZmbGluZV9hYzciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9ldnNfcmV0eXBlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfaW50ZXJuYWwiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9rb29tYXAiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9ldnNfZXNzZDIiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kbXMtYW1xcC1iYXNpYyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2V2c19wb29sX2NhIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYV9jbi1zb3V0aHdlc3QtMmIiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9od2NwaCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Vjc19vZmZsaW5lX2Rpc2tfNCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2h3ZGV2IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfc21uX3dlbGlua3JlZCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2h2X3ZlbmRvciIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfY24tbm9ydGgtNGUiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hX2NuLW5vcnRoLTRkIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWNzX2hlY3NfeCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Nicl9maWxlc19iYWNrdXAiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3NfYWM3IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY3Nic19yZXN0b3JlX2FsbCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfY24tbm9ydGgtNGYiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9vcF9nYXRlZF9yb3VuZHRhYmxlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZXZzX2V4dCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Bmc19kZWVwX2FyY2hpdmUiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hX2FwLXNvdXRoZWFzdC0xZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfcnUtbW9zY293LTFiIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYV9hcC1zb3V0aGVhc3QtMWQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hcHBzdGFnZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FfYXAtc291dGhlYXN0LTFmIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfc21uX2FwcGxpY2F0aW9uIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZXZzX2NvbGQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9yZHNfY2EiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3NfZ3B1X2c1ciIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX29wX2dhdGVkX21lc3NhZ2VvdmVyNWciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3NfcmkiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9hX3J1LW5vcnRod2VzdC0yYyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2llZl9wbGF0aW51bSIsImlkIjoiMCJ9LHsibmFtZSI6IjI1OSwxMjcsMTk4LDEwOCwyMjMsODQsMTQ0LDcwLDE0MSw3OSw2NiwwLDI2MCwyNDgsODEsMTI1LDQwLDE3NCw3LDIwOCw5NSwzMiwxMCwyMTEsMTYsNjMsNTgsNzUsMTIzLDE4MCwxNzcsMTg2LDMwLDEzMCwyNTEsMjAyLDEyMCwxNjcsMzgsNTQsMjM0LDE0OSw4MywyMTMsMTk1LDQ4LDI1NSwyMzEsMTUzLDE5MCwxMDQsMTAwMSwzLDIwNiwxMzMsMTgyLDkxLDE4OCwyOSw0NSwzNCwzNiwxMjIsMjE4LDI1NiwxNCwxNzAsMjUsMTM4LDc4LDE3OCw0MiwxMDcsMzksMjAxLDEyLDg3LDUwLDEwMCwxNjQsMTMyLDI4LDE1NSwyMjcsNTYsMTExLDExNSwyNjEsNjksMTUsMTg0LDExNCwxMzksMTAyLDI1NywyMTUsOTksMTQ3LDE1MCw3MywyMyw2LDIzNywyMjAsNTksMTU3LDEzNSwyMzAsNDksMjU4LDExMyw5NiIsImlkIjoiOCJ9LHsibmFtZSI6IjEsMCIsImlkIjoiOSJ9LHsibmFtZSI6Im9wX2ZpbmVfZ3JhaW5lZCIsImlkIjoiNyJ9XSwicHJvamVjdCI6eyJkb21haW4iOnsibmFtZSI6Imh3c3RhZmZfcHViX1RSQ0Nsb3VkVGVhbSIsImlkIjoiOWYxYTAxN2UzMWEwNDQ4OWE1NjU3MmE1NTk5MjRmN2MifSwibmFtZSI6ImFwLXNvdXRoZWFzdC0zIiwiaWQiOiIwNGU4ZTViNDQ4MDAwZmJmMmZiNmMwMDgxZmNmMmI1YyJ9LCJpc3N1ZWRfYXQiOiIyMDI1LTA2LTEzVDEwOjA4OjEzLjM4MDAwMFoiLCJ1c2VyIjp7ImRvbWFpbiI6eyJuYW1lIjoiaHdzdGFmZl9wdWJfVFJDQ2xvdWRUZWFtIiwiaWQiOiI5ZjFhMDE3ZTMxYTA0NDg5YTU2NTcyYTU1OTkyNGY3YyJ9LCJuYW1lIjoiaXRhaV9nZW5kbGVyIiwicGFzc3dvcmRfZXhwaXJlc19hdCI6IiIsImlkIjoiNDQ5NzgzYTE1MDg0NGFlM2FjZjUwM2Y3YzZkZjU1OWMifX19MYIBwTCCAb0CAQEwgZcwgYkxCzAJBgNVBAYTAkNOMRIwEAYDVQQIDAlHdWFuZ0RvbmcxETAPBgNVBAcMCFNoZW5aaGVuMS4wLAYDVQQKDCVIdWF3ZWkgU29mdHdhcmUgVGVjaG5vbG9naWVzIENvLiwgTHRkMQ4wDAYDVQQLDAVDbG91ZDETMBEGA1UEAwwKY2EuaWFtLnBraQIJANyzK10QYWoQMAsGCWCGSAFlAwQCATANBgkqhkiG9w0BAQEFAASCAQCPyCc7KkiLmZ0bkzYPn8I+qCnpiplBjxhZOdyv0tzT2J7YVVoZQHj1KzY8ISCrx3kKhEGdk1LtcJGheysoExJ3w7clVBWUJcBZ+SKIBGE4mLxOXYbaKCJelBpM7rZcou8zN8Mhh8fYK442YDJNOqwr5t97RIbP-AO7t3KgLR8nBf22drK9pycBvpJSYZlnebeoJejeSYY87dxIO2KOyJB+YjVOd38Em2ZqYWXWHK6eBtn5LjZxB0ahk9usXyO2T8yvk1856+Dlzw1hj5CZc6Gx1g8FWYvVKjRBKVnfR+6psfS1jABanoaooQ9dKxNbruAxnS-3admiGhg-rVxESUbr',
    'x-language': 'en-us',
    'Content-Type': 'application/json',
    'Cookie': 'HWWAFSESID=625e6738b7379857f2; HWWAFSESTIME=1749809286262'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    # write response | .[0].data[0].layout_content to file
    # chars might be chineese
    with open(plugin_name + ".json", "w", encoding="utf-8") as f:
        try:
            resp_json = response.json()
            data = resp_json[0].get("data", [])
            if data and data[0].get("layout_content"):
                # Only parse if layout_content is not None
                f.write(json.dumps(json.loads(data[0]["layout_content"]), ensure_ascii=False, indent=2))
            else:
                # write: data is empty
                f.write("data is empty []")
        except Exception as error:
            print('response: ', response.json())
            print(error)
            f.write("can't write")
