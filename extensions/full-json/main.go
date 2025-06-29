package main

// outer json structs
type PluginPartQueryVOListAgentPluginInputVO struct {
	Data []Data // list of inputs
}

type Data struct {
	LayoutContent []DForm
}

// d-form -> d-form-item (props,children) -> d-custom-component (props,children)

// input, len(children) = len(intput)
type DForm struct {
	Children []DFormItem
}

type DFormItem struct {
	Props    DFormItemProps
	Children []DCustomComponent
}

type DFormItemProps struct {
	Label    string // should help
	Field    string // input.key
	HelpTips string // should help
	// verification
	Rules []DFormItemRules // need to enforce required / regex // optional
	// advanced
	// display by condition
	Visible struct {
		Type       string // check if type === 'condition'
		Conditions []Condition
	}
}

type Condition struct {
	Comp   string // widget_id
	Symbol string // =
	Value  string // value
}

type DFormItemRules struct {
	Required *bool
	Regex    *string
	Message  string
}

type DCustomComponent struct {
	ComponentName DCustomComponentName // data type!
	Props         DCustomComponentProps
}

type DCustomComponentProps struct {
	DefaultValue string
	// advanced
	// disabled by condition
	Disabled struct {
		Type       string // check if type === 'condition'
		Conditions []Condition
	}

	// special props
	MaxLength int // d-textarea
	Precision int // d-input-number
	ShowPlaceholder string // d-input

	MultipleOptions Option // multiple-select
	SingleOptions   Option // d-radio-group, d-select
}

type Option struct {
	Type         string // fixed, api, context
	FixedOptions []FixedOption
	ApiOptions   ApiOption
	DataSource   string // repoSource, buildTasks
}

type FixedOption struct {
	Label string
	Value string
	DefaultChecked bool
}

type ApiOption struct {

	Url string
	Method string // GET / POST
	Params map[string]string
	Header map[string]string
	Body map[string]any

	Label string
	Value string

	ResponseUrl string

	LinkedFields []string // widget ids

	Remote bool
	RemoteName string
	RemoteQueryField string // params / body
	SearchTips string
}

type DCustomComponentName string

const (
	DCustomComponentNameString            DCustomComponentName = "d-input"         // Single-line Text Box -> string
	DCustomComponentNameArray             DCustomComponentName = "d-input-number"  // Digit
	DCustomComponentNameSelect            DCustomComponentName = "d-select"        // Single-selection Drop-down List
	DCustomComponentNameMultipleSelect    DCustomComponentName = "multiple-select" // Multi-selection Drop-down List
	DCustomComponentNameBoolean           DCustomComponentName = "d-switch"        //Switch -> true or false
	DCustomComponentNameObject            DCustomComponentName = "input"
	DCustomComponentNameTextarea          DCustomComponentName = "d-textarea"         // Multi-line Text Box
	DCustomComponentNameRadio             DCustomComponentName = "d-radio-group"      // Button Option
	DCustomComponentNameBuildPackage      DCustomComponentName = "build-package"      // Building Product
	DCustomComponentNameDeployPackage     DCustomComponentName = "deploy-package"     // Chose Package
	DCustomComponentNameTimeInterval      DCustomComponentName = "time-interval"      // Time Interval
	DCustomComponentNameInterface         DCustomComponentName = "interface"          // API
	DCustomComponentNameTaskParameter     DCustomComponentName = "task-parameter"     // Parameters
	DCustomComponentNameLinkSelect        DCustomComponentName = "link-select"        // Hyperlink Drop Down List Box
	DCustomComponentNameKeyValue          DCustomComponentName = "key-value"          // Parameters -> "[{\"key\":\"key1\",\"value\":\"value1\"}]"
	DCustomComponentNameInterfaceTextarea DCustomComponentName = "interface-textarea" // Interface Text Box
	DCustomComponentNameJsonInput         DCustomComponentName = "json-input"         // Object Input
	DCustomComponentNameShell             DCustomComponentName = "shell"              // Shell
)

// rules - from outer json
//1. len(.data[]) is len(inputs[])
//2. .data[].name == inputs[].key
//3. .data[].type == inputs[].type
//4. .data[].default_value == inputs[].default_value
//5. please ignore key_1667031515150

// rules - from inner json
//1. len([0].children[]) == len(.inputs[])
//2. [0].children[].props.field == .inputs[].key
//3. [0].children[].props.help-tips should help
// len([0].children[].props.rules[]) == 2
//4. [0].children[].props.rules[0] is required, = valudation
//5. [0].children[].props.rules[1] is regex, = validation
