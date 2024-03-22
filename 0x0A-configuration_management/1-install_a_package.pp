# Using Puppet, install flask from pip3
package { 'puppet-line':
  ensure   => '2.1.0',
  provider => 'gem',
}
