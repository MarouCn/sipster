{
  'targets': [
    {
      'target_name': 'sipster',
      'sources': [
        'src/binding.cc',
        'src/SIPSTERAccount.cc',
        'src/SIPSTERCall.cc',
        'src/SIPSTERMedia.cc',
        'src/SIPSTERTransport.cc',
      ],
      'include_dirs': [
        "src",
        "<!(node -e \"require('nan')\")"
      ],
      'cflags_cc+': ['-g3'],
      'conditions': [
        [ 'OS=="mac"', {
          'cflags_cc': [
            '<!@(pkg-config --atleast-version=2.4.5 libpjproject)',
            '<!@(pkg-config --cflags libpjproject)',
            '-fexceptions',
            '-Wno-maybe-uninitialized',
          ],
          'xcode_settings': {
            'OTHER_CFLAGS': [
              '-fexceptions',
              '-frtti',
            ]
          },
        }],
      ],
    },
  ],
}
