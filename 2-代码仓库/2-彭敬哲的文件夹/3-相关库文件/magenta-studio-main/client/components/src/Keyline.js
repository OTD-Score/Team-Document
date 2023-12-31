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

import { LitElement, html } from 'lit'
// import './File'
import './Select'
import './Tabs'
import './Ableton'

class Keyline extends LitElement {

	render(){
		return html`
			<style>
				:host {

				}

				div {
					margin: 10px 0;
					width: 100%;
					height: 1px;
					border-bottom: 2px solid var(--color-gray);
				}

			</style>
			<div></div>
		`
	}
}
customElements.define('magenta-keyline', Keyline)
