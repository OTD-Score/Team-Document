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

const models = {
	drums : new Model(true),
	melody : new Model(false),
}

async function generate(){

	if (!validate()){
		return
	}
	setStatus('Generating...')
	//get all the attributes
	const mode = document.querySelector('#mode').value
	const steps = document.querySelector('#variations').value
	const temp = document.querySelector('#temperature').value
	try {
		const [inputMidiA, inputMidiB] = await document.querySelector('magenta-midi-file').read()
		const output = await models[mode].predict(inputMidiA, inputMidiB, steps, temp)
		await document.querySelector('magenta-midi-file').write(output, 'INTERPOLATE')
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

if (ANIMATE){
	//title animation
	setInterval(() => {
		if (document.querySelector('#title').classList.contains('hover')){
			document.querySelector('#title').classList.remove('hover')
		} else {
			document.querySelector('#title').classList.add('hover')
		}
	}, 500)
}

export function Interpolate(parentElement){
	const initialized = Promise.all([models.drums.load(), models.melody.load()])
	initialized.then(() => {
		setStatus('')
	})
	render(html`
		<div id="interpolate">
			<div id="title">
				<span>I</span>
				<span class="expand">N</span>
				<span class="expand">T</span>
				<span class="expand">E</span>
				<span class="expand">R</span>
				<span class="expand">P</span>
				<span class="expand">O</span>
				<span class="expand">L</span>
				<span class="expand">A</span>
				<span>T</span>
				<span>E</span>
			</div>
			<div class="plugin-content">
				<div id="controls">
					<div class="plugin-panel__type">
						<magenta-radio-group
								label="Type"
								values=${JSON.stringify(['drums', 'melody'])}
								id="mode">
							</magenta-radio-group>
					</div>
					<div class="plugin-panel">
						<magenta-midi-file label="Input Clips" @change=${validate} inputs="2"></magenta-midi-file>
					</div>
					<div class="plugin-panel__generate">
						<magenta-output-text></magenta-output-text>
						<magenta-button id="generate" label="Initializing..." disabled @click=${generate}></magenta-button>
					</div>
					<div class="plugin-panel">
						<magenta-slider id="variations" value="3" min="1" max="16" label="Steps"></magenta-slider>
						<magenta-slider id="temperature" value="1" min="0" max="2" step="0.1" label="Temperature"></magenta-slider>
					</div>
				</div>
			</div>
		</div>
	`, parentElement)
}

