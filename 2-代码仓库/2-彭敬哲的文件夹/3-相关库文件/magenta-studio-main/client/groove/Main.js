/**
 * @license
 * Copyright 2018 Google Inc. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { render, html } from 'lit'
import { Model } from './Model'
import './style.scss'

const model = new Model()

async function generate(){
	if (!validate()){
		return
	}
	setStatus('Generating...')
	//get all the attributes
	const temp = document.querySelector('#temperature').value
	// const variations = document.querySelector('#variations').value
	try {
		const inputMidi = await document.querySelector('magenta-midi-file').read()
		const output = await model.unquantize(inputMidi, temp)
		await document.querySelector('magenta-midi-file').write([output], 'GROOVE')
	} catch (e){
		const snackbar = document.createElement('magenta-snackbar')
		snackbar.setAttribute('message', e)
		snackbar.setAttribute('error', '')
		snackbar.setAttribute('whoops', '')
		document.body.appendChild(snackbar)
		setStatus('')
		throw e
	}
	setStatus('')
}

function validate(){
	if (controls.classList.contains('generating')){
		return false
	}
	const valid = document.querySelector('magenta-midi-file').valid
	const button = document.querySelector('#generate')
	if (valid){
		button.removeAttribute('disabled')
	} else {
		button.setAttribute('disabled', '')
	}
	return valid
}

// <magenta-slider id="temperature" value="1" min="0" max="2" step="0.1" label="Temperature"></magenta-slider>
// <magenta-slider id="variations" value="4" min="1" max="8" label="Variations"></magenta-slider>

function setStatus(status, error=false){
	const element = document.querySelector('magenta-button')
	const controls = document.querySelector('#controls')
	if (status === ''){
		element.setAttribute('label', 'Generate')
		controls.classList.remove('generating')
	} else {
		element.setAttribute('label', status)
		controls.classList.add('generating')
	}
}

export function Groove(parentElement){
	model.load().then(() => {
		setStatus('')
	})

	render(html`
		<div id="groove">
			<div id="title" class="${ANIMATE ? 'animate' : ''}">
				<span>G</span>
				<span>R</span>
				<span>O</span>
				<span>O</span>
				<span>V</span>
				<span>E</span>
			</div>
			<div class="plugin-content">
				<div id="controls">
					<div class="plugin-panel__type">
						<magenta-radio-group
							label="Type"
							values=${JSON.stringify(['drums'])}
							id="mode">
					</div>
					<div class="plugin-panel">
						</magenta-radio-group>
							<magenta-midi-file
								label="Input Clip"
								@change=${validate}></magenta-midi-file>
					</div>
					<div class="plugin-panel__generate">
						<magenta-output-text></magenta-output-text>
						<magenta-button disabled id="generate" label="Initializing..." @click=${generate}></magenta-button>
					</div>
					<div class="plugin-panel">
						<magenta-slider id="temperature" value="1" min="0" max="2" step="0.1" label="Temperature"></magenta-slider>
					</div>
				</div>
			</div>
		</div>
	`, parentElement)
}
